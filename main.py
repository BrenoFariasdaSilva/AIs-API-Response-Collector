import atexit # For playing a sound when the program finishes
import csv # For reading and writing CSV files
import os # For running a command in the terminal
import numpy as np # For numerical operations
import pandas as pd # For reading CSV files
import sys # For exiting the program
from chatgpt import ChatGPTModel # Import the ChatGPTModel class from ./chatgpt.py
from colorama import Style # For coloring the terminal
from copilot import CopilotModel # Import the CopilotModel class from ./copilot.py
from gemini import GeminiModel # Import the GeminiModel class from ./gemini.py
from llama import LlamaModel # Import the LlamaModel class from ./llama.py
from mistral import MistralModel # Import the MistralModel class from ./mistral.py
from sklearn.feature_extraction.text import TfidfVectorizer # For calculating Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity # To compute similarity
from utils import BackgroundColors # Import Classes from ./utils.py
from utils import START_PATH, OUTPUT_DIRECTORY # Import Constants from ./utils.py
from utils import create_directory, play_sound, verbose_output # Import Functions from ./utils.py

# Execution Constants:
EXECUTE_MODELS = {"ChatGPT": "ChatGPTModel", "Copilot": "CopilotModel", "Gemini": "GeminiModel", "Llama": "LlamaModel", "Mistral": "MistralModel"} # The AI/LLM models to execute

# Input/Output Directory Constants:
INPUT_DIRECTORY = f"{START_PATH}/Inputs/" # The path to the input directory

# Input/Output File Path Constants:
INPUT_CSV_FILE = f"{INPUT_DIRECTORY}input.csv" # The path to the input CSV file
OUTPUT_CSV_FILE = f"{OUTPUT_DIRECTORY}output.csv" # The path to the output CSV file

def create_directories():
   """
   Creates the input and output directories.

   :return: None
   """

   create_directory(INPUT_DIRECTORY, INPUT_DIRECTORY.replace(START_PATH, "")) # Create the input directory
   create_directory(OUTPUT_DIRECTORY, OUTPUT_DIRECTORY.replace(START_PATH, "")) # Create the output directory

def read_csv_file():
   """
   Reads tasks from the input CSV file using pandas and returns the DataFrame.

   :return: None
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Reading tasks from CSV file using pandas...{Style.RESET_ALL}") # Output the reading message

   if os.path.exists(INPUT_CSV_FILE): # If the input CSV file exists
      df = pd.read_csv(INPUT_CSV_FILE) # Reading the CSV into a DataFrame
      return df # Return the DataFrame
   else: # If the input CSV file does not exist
      print(f"{BackgroundColors.RED}CSV file {BackgroundColors.CYAN}{INPUT_CSV_FILE}{BackgroundColors.RED} not found. Make sure the file exists.{Style.RESET_ALL}")
      sys.exit(1) # Exit the program

def get_models_object_list(models_object_names=EXECUTE_MODELS.values()):
   """
   Get the list of objects of the AI models.

   :param models_object_names: The list of AI model object names.
   :return: The list of AI model objects.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Getting the list of AI model objects...{Style.RESET_ALL}") # Output the getting message
   
   model_objects = [] # Initialize the list of model objects
   
   for model_object_name in models_object_names: # Loop through each model object name
      try: # Try to get the model object
         model_class = globals()[model_object_name] # Get the model class from the globals
         model_objects.append(model_class()) # Append the model object to the list
      except KeyError: # If the model object is not found
         print(f"{BackgroundColors.RED}Error: Model class '{model_object_name}' not found in globals.{Style.RESET_ALL}")
      except Exception as e: # If an error occurs
         print(f"{BackgroundColors.RED}Error instantiating model '{model_object_name}': {str(e)}{Style.RESET_ALL}")

   return model_objects # Return the list of model objects

def initialize_dict(models_list):
   """
   Initialize a dictionary with empty lists based on the models' module names, and include fields for "Expected Output" and similarity scores for the most similar models.

   :param models_list: The list of model objects.
   :return: The initialized dictionary.
   """
   
   verbose_output(true_string=f"{BackgroundColors.GREEN}Initializing the output dictionary...{Style.RESET_ALL}") # Output the initialization message

   output_dict = { # Initialize the output dictionary
      "Task": [], # Placeholder for task descriptions
      "Expected Output": [], # Placeholder for expected outputs
      "Most Similar Model": [], # Placeholder for the most similar model names
      "Minimum Similarity": [], # Placeholder for minimum similarity
      "Maximum Similarity": [], # Placeholder for maximum similarity
      "Average Similarity": [], # Placeholder for average similarity
      "Median Similarity": [], # Placeholder for median similarity
      "Standard Deviation Similarity": [], # Placeholder for standard deviation of similarity
   }

   for model in models_list: # Add model names and similarity fields dynamically
      model_name = model.__module__.split(".")[-1].capitalize() # Extract model name
      output_dict[model_name] = [] # Initialize an empty list for the model output
      output_dict[f"{model_name} Similarity"] = [] # Initialize an empty list for similarity scores

   return output_dict # Return the initialized dictionary

def get_task_description(task):
   """
   Get the task description from the task DataFrame.

   :param task: The task from the DataFrame.
   :return: The task description.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Getting the task description...{Style.RESET_ALL}") # Output the getting message

   return task["Task"] # Get the task description from the task

def get_expected_output(task):
   """
   Get the expected output from the task, if available.

   :param task: The task from the DataFrame.
   :return: The expected output or an empty string if not present.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Getting the expected output from the task...{Style.RESET_ALL}") # Output the getting message

   return task.get("Expected Output (Optional)", "") # Get the expected output from the task

def get_tasks_attributes(task):
   """
   Get the task description and expected output from the task DataFrame.

   :param task: The task row from the DataFrame.
   :return: Tuple of task_description and expected_output.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Getting the task description and expected output...{Style.RESET_ALL}") # Output the getting message

   task_description = get_task_description(task) # Get the task description
   expected_output = get_expected_output(task) # Get the expected output

   return task_description, expected_output # Return the task description and expected output

def update_output_dict(output_dict, task_description, expected_output):
   """
   Update the output dictionary with the task description and expected output.

   :param output_dict: The output dictionary to update.
   :param task_description: The task description.
   :param expected_output: The expected output.
   :return: None
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Updating the output dictionary with the task description and expected output...{Style.RESET_ALL}") # Output the updating message

   output_dict["Task"].append(task_description) # Add the task description to the dictionary
   output_dict["Expected Output"].append(expected_output) # Add the expected output to the dictionary

def format_output(output):
   """
   Format the output by:
   1. Removing extra newlines and empty lines.
   2. Replacing single newline characters with ' // '.
   3. Removing ' // ' between empty or whitespace-only lines.
   
   :param output: The output string to format.
   :return: The formatted string.
   """

   lines = [line.strip() for line in output.splitlines() if line.strip()] # Split the output into lines and filter out lines that are empty or contain only whitespaces
   
   return " // ".join(lines) # Join the lines with " // "

def run_task_on_each_model(models_object_list, task_description, output_dict):
   """
   Run the task on each AI model and store the results in the output dictionary.

   :param models_object_list: The list of AI model objects.
   :param task_description: The description of the task to run.
   :param output_dict: The output dictionary to store results.
   :return: A dictionary of task results from all models.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Running the task on each AI model...{Style.RESET_ALL}") # Output the running message

   task_results = {} # Initialize the task results dictionary
   for model in models_object_list: # Loop through each model object
      model_name = model.__module__.split(".")[-1].capitalize() # Get the model's name
      result = model.run(task_description) # Run the task using the model's "run" method
      formatted_output = format_output(result) # Format the output
      task_results[model_name] = formatted_output # Add the result to the task results dictionary
      output_dict[model_name].append(format_output(formatted_output)) # Add the result to the output dictionary

   return task_results # Return the task results dictionary

def compute_similarity(output, expected_output):
   """
   Compute the similarity between the output and the expected output using Cosine Similarity.

   :param output: The output text.
   :param expected_output: The expected output text.
   :return: The similarity percentage.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Computing the similarity between the output and the expected output...{Style.RESET_ALL}") # Output the computation message

   if pd.isna(expected_output) or not expected_output.strip(): # If the expected output is empty
      return None # Return None
   
   vectorizer = TfidfVectorizer().fit_transform([output, expected_output]) # Fit the vectorizer and transform the output and expected output
   vectors = vectorizer.toarray() # Convert the vectorizer to an array
   similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0] # Compute the cosine similarity between the vectors

   return round(similarity * 100, 2) # Return similarity as a percentage rounded to 2 decimal places

def compute_similarity_statistics(similarity_scores):
   """
   Compute min, max, average, median, and standard deviation of similarity scores.

   :param similarity_scores: List of tuples with model names and their similarity scores.
   :return: Tuple of min_similarity, max_similarity, average_similarity, median_similarity, and standard_deviation_similarity.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Computing similarity statistics...{Style.RESET_ALL}") # Output the computation message

   valid_scores = [score for model_name, score in similarity_scores if isinstance(score, (int, float))] # Extract valid numeric scores, ensuring they are floats

   if not valid_scores: # Handle case with no valid scores
      return (0, 0, 0, 0, 0) # Or another appropriate value for empty case

   min_similarity = round(min(valid_scores), 2) # Compute the minimum similarity
   max_similarity = round(max(valid_scores), 2) # Compute the maximum similarity
   average_similarity = round(np.mean(valid_scores), 2) # Compute the average similarity
   median_similarity = round(np.median(valid_scores), 2) # Compute the median similarity
   standard_deviation_similarity = round(np.std(valid_scores), 2) # Compute the standard deviation

   statistics_tuple = (min_similarity, max_similarity, average_similarity, median_similarity, standard_deviation_similarity) # Store the statistics in a tuple

   return statistics_tuple # Return the statistics

def update_similarity_statistics(output_dict, statistics_tuple):
   """
   Update the output dictionary with similarity statistics.

   :param output_dict: The output dictionary to update.
   :param statistics_tuple: Tuple of min_similarity, max_similarity, average_similarity, median_similarity, and standard_deviation_similarity.
   :return: None
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Updating the output dictionary with similarity statistics...{Style.RESET_ALL}") # Output the updating message

   output_dict["Minimum Similarity"].append(statistics_tuple[0]) # Update the minimum similarity
   output_dict["Maximum Similarity"].append(statistics_tuple[1]) # Update the maximum similarity
   output_dict["Average Similarity"].append(statistics_tuple[2]) # Update the average similarity
   output_dict["Median Similarity"].append(statistics_tuple[3]) # Update the median similarity
   output_dict["Standard Deviation Similarity"].append(statistics_tuple[4]) # Update the standard deviation similarity

def compute_similarity_for_models(models_object_list, task_results, expected_output, output_dict):
   """
   Compute similarity scores for each model and update the output dictionary.

   :param models_object_list: List of model objects.
   :param task_results: The results from running the task on the models.
   :param expected_output: The expected output for the task.
   :param output_dict: The output dictionary to store results.
   :return: List of similarity scores for each model.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Computing similarity scores for each model...{Style.RESET_ALL}") # Output the computation message

   similarity_scores = [] # To store similarity scores for each model

   for model in models_object_list: # Loop through each model object
      model_name = model.__module__.split(".")[-1].capitalize() # Get model's name
      similarity_score = compute_similarity(task_results[model_name], expected_output) # Compute similarity score
      similarity_scores.append((model_name, similarity_score if similarity_score is not None else 0)) # Append the model name and similarity score to the list
      output_dict[f"{model_name} Similarity"].append(similarity_score if similarity_score is not None else "N/A") # Append the similarity score for each model
   
   statistics_tuple = compute_similarity_statistics(similarity_scores) # Compute similarity statistics
   update_similarity_statistics(output_dict, statistics_tuple) # Update similarity statistics

   return similarity_scores # Return the list of similarity scores

def update_most_similar_model(similarity_scores, output_dict):
   """
   Update the output dictionary with the most similar model based on similarity scores.

   :param similarity_scores: List of tuples with model names and their similarity scores.
   :param output_dict: The output dictionary to store the most similar model.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Updating the most similar model in the output dictionary...{Style.RESET_ALL}") # Output the updating message

   most_similar_model, overall_similarity_score = max(similarity_scores, key=lambda x: (x[1] is not None, x[1])) # Get the most similar model and score
   output_dict["Most Similar Model"].append(f"{most_similar_model} ({overall_similarity_score}%)") # Update most similar model

def run_tasks(df):
   """
   Run the tasks in the DataFrame.

   :param df: The DataFrame containing the tasks and the expected output.
   :return: The output dictionary.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Running the tasks for each Artificial Intelligence model...{Style.RESET_ALL}") # Output the running message

   models_object_list = get_models_object_list() # Get the list of AI model objects
   output_dict = initialize_dict(models_object_list) # Initialize the output dictionary

   for index, task in df.iterrows(): # Loop through each row in the DataFrame
      task_description, expected_output = get_tasks_attributes(task) # Get the task description and expected output
      update_output_dict(output_dict, task_description, expected_output) # Update the output dictionary with the task description and expected output
      print(f"{BackgroundColors.GREEN}Task {BackgroundColors.CYAN}{index + 1:02}{BackgroundColors.GREEN}:\n - {BackgroundColors.GREEN}Task Message: {BackgroundColors.CYAN}{task_description}{BackgroundColors.GREEN}\n - Expected Output: {BackgroundColors.CYAN}{expected_output}{Style.RESET_ALL}\n") # Output the task description and expected output

      task_results = run_task_on_each_model(models_object_list, task_description, output_dict) # Run the task on each AI model

      similarity_scores = compute_similarity_for_models(models_object_list, task_results, expected_output, output_dict) # Compute similarity scores
      update_most_similar_model(similarity_scores, output_dict) # Update most similar model in the output dictionary

   return output_dict # Return the output list

def convert_dict_to_df(output_dict):
   """
   Convert the output dictionary to a DataFrame.

   :param output_dict: The output dictionary.
   :return: The output DataFrame.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Converting the output dictionary to a DataFrame...{Style.RESET_ALL}") # Output the conversion message

   return pd.DataFrame(output_dict) # Return the DataFrame

def write_output_to_csv(output_dict):
   """
   Write the output to a new CSV file with the first column as the input tasks and the other columns as the AI model outputs.

   :param output_dict: The output dictionary containing model outputs.
   :return: None
   """
   
   verbose_output(true_string=f"{BackgroundColors.GREEN}Writing the output to the output CSV file...{Style.RESET_ALL}") # Output the writing message

   try: # Try to write the output to the CSV file
      with open(OUTPUT_CSV_FILE, mode="w", newline="", encoding="utf-8") as file: # Open the output CSV file
         writer = csv.writer(file) # Create a CSV writer
         writer.writerow(output_dict.keys()) # Write the header row

         num_rows = len(output_dict["Task"]) # Get the number of rows based on the length of the "Task" list
         for i in range(num_rows): # Loop through each row
            row = [output_dict[key][i] for key in output_dict] # Get the values for each key in the dictionary
            writer.writerow(row) # Write the row to the CSV file
      
      verbose_output(true_string=f"{BackgroundColors.GREEN}Output written to {BackgroundColors.CYAN}{OUTPUT_CSV_FILE}{Style.RESET_ALL}") # Output the success message
   except Exception as e: # If an error occurs
      print(f"{BackgroundColors.RED}Error writing output to CSV: {str(e)}{Style.RESET_ALL}") # Output the error message

def main():
   """
   Main function.

   :return: None
   """

   print(f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}AIs API Response Collector{BackgroundColors.GREEN}!{Style.RESET_ALL}\n") # Output the welcome message

   create_directories() # Create the input and output directories

   tasks_df = read_csv_file() # Read the tasks from the input CSV file
   output_dict = run_tasks(tasks_df) # Run the tasks
   write_output_to_csv(output_dict) # Write the output to the output CSV file

   print(f"{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}") # Output the end of the program message
   atexit.register(play_sound) # Register the function to play a sound when the program finishes

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
