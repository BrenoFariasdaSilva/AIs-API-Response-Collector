# API Guide: https://platform.openai.com/docs/quickstart?language-preference=python

import atexit # For playing a sound when the program finishes
import os # For running a command in the terminal
import sys # For exiting the program
from colorama import Style # For coloring the terminal
from dotenv import load_dotenv # For loading .env files
from openai import OpenAI # Import OpenAI client
from utils import BackgroundColors # Import Classes from ./utils.py
from utils import OUTPUT_DIRECTORY # Import Constants from ./utils.py
from utils import create_directory, play_sound, verbose_output, verify_filepath_exists, write_output_to_file # Import Functions from ./utils.py

class ChatGPTModel:
	"""
	A class to interact with the ChatGPT AI model.

	"""

	# Constants:
	ENV_PATH = "./.env" # The path to the .env file
	ENV_VARIABLE = "CHATGPT_API_KEY" # The environment variable to load
	OUTPUT_FILE = f"{OUTPUT_DIRECTORY}ChatGPT_output.txt" # The path to the output file

	def __init__(self): # Constructor
		self.api_key = self.verify_env_file()  # Call verify_env_file to load the API key
		self.model = "gpt-4o-mini" # The AI model
		self.client = OpenAI(api_key=self.api_key)  # Initialize the OpenAI client with the API key

	def verify_env_file(self, env_path=ENV_PATH, key=ENV_VARIABLE):
		"""
		Verify if the .env file exists and if the desired key is present.

		:param env_path: Path to the .env file.
		:param key: The key to get in the .env file.
		:return: The value of the key if it exists.
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Verifying the .env file...{Style.RESET_ALL}") # Output the verification message

		if not verify_filepath_exists(env_path): # If the .env file does not exist
			print(f"{BackgroundColors.RED}.env file not found at {BackgroundColors.CYAN}{env_path}{Style.RESET_ALL}") # Output the error message
			sys.exit(1) # Exit the program

		load_dotenv(env_path) # Load the .env file
		api_key = os.getenv(key) # Get the value of the key

		if not api_key: # If the key does not exist
			print(f"{BackgroundColors.RED}Key {BackgroundColors.CYAN}{key}{BackgroundColors.RED} not found in .env file.{Style.RESET_ALL}") # Output the error message
			sys.exit(1) # Exit the program

		return api_key # Return the API key

	def run(self, task_message):
		"""
		Main function to run the AI model to do what is described in the task message.

		:param task_message: The message to send to the AI model.
		:return output: The output text.
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Running the ChatGPT AI Model...{Style.RESET_ALL}") # Output the running message

		response = self.client.chat.completions.create( # Create a completion
			model=self.model, # The model to use
			messages=[ # The messages to send
				{
					"role": "user", # The role of the user
					"content": task_message, # The content of the message
				}
			],
		)

		return response.choices[0].message # Return the response

def main():
	"""
	Main entry point to run the ChatGPTModel.

	:param None
	:return: None
	"""

	print(f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}ChatGPT AI Model{BackgroundColors.GREEN}!{Style.RESET_ALL}\n") # Output the welcome message

	chatgpt = ChatGPTModel() # Create the ChatGPTModel object
	task_message = "Explain how to create a new branch in Git." # The task message
	output = chatgpt.run(task_message) # Run the ChatGPTModel
	create_directory(os.path.abspath(OUTPUT_DIRECTORY), OUTPUT_DIRECTORY.replace(".", "")) # Create the output directory
	write_output_to_file(output, ChatGPTModel.OUTPUT_FILE) # Write the output to the file

	print(f"\n{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}") # Output the end of the program message
	atexit.register(play_sound) # Register the function to play a sound when the program finishes

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
