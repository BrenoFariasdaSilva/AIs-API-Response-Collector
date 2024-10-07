import atexit # For playing a sound when the program finishes
import os # For running a command in the terminal
import pandas as pd # For reading CSV files
import platform # For getting the operating system name
import sys # For exiting the program
from colorama import Style # For coloring the terminal
from dotenv import load_dotenv # For loading environment variables from .env file

# Macros:
class BackgroundColors: # Colors for the terminal
   CYAN = "\033[96m" # Cyan
   GREEN = "\033[92m" # Green
   YELLOW = "\033[93m" # Yellow
   RED = "\033[91m" # Red
   BOLD = "\033[1m" # Bold
   UNDERLINE = "\033[4m" # Underline
   CLEAR_TERMINAL = "\033[H\033[J" # Clear the terminal

# Execution Constants:
VERBOSE = False # Verbose mode. If set to True, it will output messages at the start/call of each function (Note: It will output a lot of messages).

# .Env Constants:
ENV_PATH = f"./.env" # The path to the .env file
ENV_VARIABLE = f"GITHUB_TOKEN" # The environment variable to load

# File Path Constants:
START_PATH = os.getcwd() # The starting path

# Input/Output Directory Constants:
INPUT_DIRECTORY = f"{START_PATH}/Inputs/" # The path to the input directory
OUTPUT_DIRECTORY = f"{START_PATH}/Outputs/" # The path to the output directory

# Input/Output File Path Constants:
INPUT_CSV_FILE = f"{INPUT_DIRECTORY}input.csv" # The path to the input CSV file
OUTPUT_CSV_FILE = f"{OUTPUT_DIRECTORY}output.csv" # The path to the output CSV file

# Sound Constants:
SOUND_COMMANDS = {"Darwin": "afplay", "Linux": "aplay", "Windows": "start"} # The commands to play a sound for each operating system
SOUND_FILE = "./.assets/Sounds/NotificationSound.wav" # The path to the sound file

def verbose_output(true_string="", false_string=""):
   """
   Outputs a message if the VERBOSE constant is set to True.

   :param true_string: The string to be outputted if VERBOSE is True.
   :param false_string: The string to be outputted if VERBOSE is False.
   :return: None
   """

   if VERBOSE and true_string != "": # If VERBOSE is True and the true_string is not empty
      print(true_string) # Output the true_string
   elif false_string != "": # If the false_string is not empty
      print(false_string) # Output the false_string

def verify_filepath_exists(filepath):
   """
   Verify if a file or folder exists at the specified path.

   :param filepath: Path to the file or folder
   :return: True if the file or folder exists, False otherwise
   """

   verbose_output(f"{BackgroundColors.YELLOW}Verifying if the file or folder exists at the path: {BackgroundColors.CYAN}{filepath}{Style.RESET_ALL}") # Output the verbose message

   return os.path.exists(filepath) # Return True if the file or folder exists, False otherwise

def get_env_token(env_path=ENV_PATH, key=ENV_VARIABLE):
   """
   Verify if the .env file exists and if the desired key is present.

   :param env_path: Path to the .env file.
   :param key: The key to get in the .env file.
   :return: The value of the key if it exists.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Verifying the .env file...{Style.RESET_ALL}")

   if not verify_filepath_exists(env_path): # Verify if the .env file exists
      print(f"{BackgroundColors.RED}The {BackgroundColors.CYAN}.env file{BackgroundColors.RED} not found at {BackgroundColors.CYAN}{env_path}{Style.RESET_ALL}")
      sys.exit(1) # Exit the program

   load_dotenv(env_path) # Load the .env file
   api_key = os.getenv(key) # Get the value of the key

   if not api_key: # Verify if the key exists
      print(f"{BackgroundColors.RED}The {BackgroundColors.CYAN}{key}{BackgroundColors.RED} key was not found in the .env file located at {BackgroundColors.CYAN}{env_path}{Style.RESET_ALL}")
      sys.exit(1) # Exit the program

   return api_key # Return the value of the key

def create_directory(full_directory_name, relative_directory_name=""):
   """
   Creates a directory.

   :param full_directory_name: Name of the directory to be created.
   :param relative_directory_name: Relative name of the directory to be created that will be shown in the terminal.
   :return: None
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Creating the {BackgroundColors.CYAN}{relative_directory_name}{BackgroundColors.GREEN} directory...{Style.RESET_ALL}")

   relative_directory_name = full_directory_name.replace(START_PATH, "") if relative_directory_name == "" else relative_directory_name # Get the relative directory name if it is not provided

   if os.path.isdir(full_directory_name): # Verify if the directory already exists
      verbose_output(f"{BackgroundColors.YELLOW}The directory already exists at the path: {BackgroundColors.CYAN}{relative_directory_name}{Style.RESET_ALL}") # Output the verbose message
      return # Return if the directory already exists
   try: # Try to create the directory
      os.makedirs(full_directory_name) # Create the directory
   except OSError: # If the directory cannot be created
      print(f"{BackgroundColors.GREEN}The creation of the {BackgroundColors.CYAN}{relative_directory_name}{BackgroundColors.GREEN} directory failed.{Style.RESET_ALL}")

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

def filter_df_by_column(df, column_name):
   """
   Filter the DataFrame by a column.

   :param df: The DataFrame to filter.
   :param column_name: The name of the column to filter by.
   :return: The filtered DataFrame.
   """

   return df[df[column_name].notnull()] # Return the filtered DataFrame

def run_tasks(df):
   """
   Run the tasks in the DataFrame.

   :param df: The DataFrame containing the tasks.
   :return: The output dictionary.
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Running the tasks for each Artificial Intelligence model...{Style.RESET_ALL}") # Output the running message

   output_dict = {} # The output dictionary

   for index, task in df.iterrows(): # Loop through each row in the DataFrame
      print(f"{BackgroundColors.GREEN}Task {index + 1}: {BackgroundColors.CYAN}{task}{Style.RESET_ALL}") # Output the task

   return output_dict # Return the output list

def convert_dict_to_df(output_dict):
   """
   Convert the output dictionary to a DataFrame.

   :param output_dict: The output dictionary.
   :return: The output DataFrame.
   """

   return pd.DataFrame(output_dict) # Return the DataFrame

def write_output_to_csv(tasks_df, output_dict):
   """
   Write the output to a new CSV file with the first column as the input tasks
   and the other columns as the AI model outputs.

   :param tasks_df: The DataFrame containing the input tasks.
   :param output_dict: The output dictionary containing model outputs.
   :return: None
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Writing the output to the output CSV file...{Style.RESET_ALL}") # Output the writing message

   output_df = convert_dict_to_df(output_dict) # Convert the output dictionary to a DataFrame
   combined_df = pd.concat([tasks_df, output_df], axis=1) # Concatenate the DataFrames along the columns
   combined_df.to_csv(OUTPUT_CSV_FILE, index=False) # Write the combined DataFrame to the output CSV file

   verbose_output(true_string=f"{BackgroundColors.GREEN}Output written to {BackgroundColors.CYAN}{OUTPUT_CSV_FILE}{Style.RESET_ALL}") # Output the success message

def play_sound():
   """
   Plays a sound when the program finishes.

   :return: None
   """

   if verify_filepath_exists(SOUND_FILE): # If the sound file exists
      if platform.system() in SOUND_COMMANDS: # If the platform.system() is in the SOUND_COMMANDS dictionary
         os.system(f"{SOUND_COMMANDS[platform.system()]} {SOUND_FILE}") # Play the sound
      else: # If the platform.system() is not in the SOUND_COMMANDS dictionary
         print(f"{BackgroundColors.RED}The {BackgroundColors.CYAN}platform.system(){BackgroundColors.RED} is not in the {BackgroundColors.CYAN}SOUND_COMMANDS dictionary{BackgroundColors.RED}. Please add it!{Style.RESET_ALL}")
   else: # If the sound file does not exist
      print(f"{BackgroundColors.RED}Sound file {BackgroundColors.CYAN}{SOUND_FILE}{BackgroundColors.RED} not found. Make sure the file exists.{Style.RESET_ALL}")

def main():
   """
   Main function.

   :return: None
   """

   print(f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}AIs API Response Collector{BackgroundColors.GREEN}!{Style.RESET_ALL}\n\n") # Output the welcome message

   get_env_token() # Get the API token from the .env file
   create_directories() # Create the input and output directories

   tasks_df = read_csv_file() # Read the tasks from the input CSV file
   filtered_df = filter_df_by_column(tasks_df, tasks_df.columns[0]) # Filter the DataFrame by the first column, which should contain the tasks
   output_dict = run_tasks(filtered_df) # Run the tasks
   write_output_to_csv(tasks_df, output_dict) # Write the output to the output CSV file

   print(f"\n{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}") # Output the end of the program message
   atexit.register(play_sound) # Register the function to play a sound when the program finishes

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
