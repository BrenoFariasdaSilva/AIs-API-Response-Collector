# API Guide: https://docs.mistral.ai/getting-started/clients/

import atexit # For playing a sound when the program finishes
import os # For running a command in the terminal
from colorama import Style # For coloring the terminal
from mistralai import Mistral # Import the Mistral client
from utils import BackgroundColors # Import Classes from ./utils.py
from utils import OUTPUT_DIRECTORY # Import Constants from ./utils.py
from utils import create_directory, play_sound, verbose_output, verify_env_file, write_output_to_file # Import Functions from ./utils.py

class MistralModel:
	"""
	A class to interact with the MistralModel AI model.

	"""

	# Constants:
	ENV_PATH = "./.env" # The path to the .env file
	ENV_VARIABLE = "MISTRAL_API_KEY" # The environment variable to load
	OUTPUT_FILE = f"{OUTPUT_DIRECTORY}Mistral_output.txt" # The path to the output file

	def __init__(self): # Constructor
		self.api_key = verify_env_file(self.ENV_PATH, self.ENV_VARIABLE) # Call verify_env_file to load the API key
		self.model_name = "mistral-large-latest" # The model name
		self.client = Mistral(api_key=self.api_key) # Initialize the Mistral client

	def run(self, task_message):
		"""
		Main function to run the AI model to do what is described in the task message.

		:param task_message: The message to send to the AI model.
		:return output: The output text.
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Running the ChatGPT AI Model...{Style.RESET_ALL}") # Output the running message

		response = self.client.chat.complete( # Get the response from the AI model
			model=self.model_name, # The model to use
			messages=[ # The messages to send
				{
					"role": "user", # The role of the user
					"content": task_message, # The content of the message
				}
			]
		)

		return response.choices[0].message.content # Return the response

def main():
	"""
	Main entry point to run the MistralModel.

	:param None
	:return: None
	"""

	print(f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}MistralModel AI Model{BackgroundColors.GREEN}!{Style.RESET_ALL}\n") # Output the welcome message

	mistral = MistralModel() # Create the MistralModel object
	task_message = "Explain how to create a new branch in Git." # The task message
	output = mistral.run(task_message) # Run the MistralModel
	create_directory(os.path.abspath(OUTPUT_DIRECTORY), OUTPUT_DIRECTORY.replace(".", "")) # Create the output directory
	write_output_to_file(output, MistralModel.OUTPUT_FILE) # Write the output to the file

	print(f"\n{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}") # Output the end of the program message
	atexit.register(play_sound) # Register the function to play a sound when the program finishes

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
