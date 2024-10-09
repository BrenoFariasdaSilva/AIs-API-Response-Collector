# API Guide: https://ai.google.dev/gemini-api/docs/quickstart?lang=python

import atexit # For playing a sound when the program finishes
import google.generativeai as genai # Import the Google AI Python SDK
import os # For running a command in the terminal
from colorama import Style # For coloring the terminal
from utils import BackgroundColors # Import Classes from ./utils.py
from utils import OUTPUT_DIRECTORY # Import Constants from ./utils.py
from utils import create_directory, play_sound, verbose_output, verify_env_file, write_output_to_file # Import Functions from ./utils.py

class GeminiModel:
	"""
	A class to interact with the Google Gemini AI model.

	"""

	# Constants:
	ENV_PATH = "./.env" # The path to the .env file
	ENV_VARIABLE = "GEMINI_API_KEY" # The environment variable to load
	OUTPUT_FILE = f"{OUTPUT_DIRECTORY}Gemini_output.txt" # The path to the output file

	def __init__(self): # Constructor
		self.api_key = verify_env_file(self.ENV_PATH, self.ENV_VARIABLE) # Verify the .env file and load the API key
		self.model_name = "gemini-1.5-flash" # The model name
		self.model = None # The AI model
	
	def configure_model(self, api_key):
		"""
		Configures the Gemini AI model.

		:param api_key: The API key for configuration.
		:return: The configured model.
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Configuring the Gemini Model...{Style.RESET_ALL}") # Output the configuration message

		genai.configure(api_key=api_key) # Configure the API key

		generation_config = { # Generation configuration
			"temperature": 0.1, # Temperature
			"top_p": 0.95, # Top p
			"top_k": 64, # Top k
			"max_output_tokens": 8192, # Maximum output tokens
		} # Generation configuration

		model = genai.GenerativeModel( # Create the model
			model_name=self.model_name, # Model name
			generation_config=generation_config, # Generation
		)

		return model # Return the model
	
	def start_chat_session(self, model, initial_user_message):
		"""
		Starts a chat session with the model.

		:param model: The AI model.
		:param initial_user_message: The initial message to start the session.
		:return: The chat session.
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Starting the chat session...{Style.RESET_ALL}") # Output the chat session message

		chat_session = model.start_chat( # Start the chat session
			history=[ # History
				{
					"role": "user", # Role
					"parts": [initial_user_message], # Parts
				}
			]
		)

		return chat_session # Return the chat session
	
	def send_message(self, chat_session, user_message):
		"""
		Sends a message to the chat session and gets the output.

		:param chat_session: The current chat session.
		:param user_message: The message to send.
		:return: The output from the model.
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Sending the message...{Style.RESET_ALL}") # Output the sending message

		output = chat_session.send_message(user_message) # Send the message
		return output.text # Return the output text

	def run(self, task_message):
		"""
		Main function to run the AI model to do what is described in the task message.

		:param task_message: The message to send to the AI model.
		:return output: The output text.
		"""

		self.model = self.configure_model(self.api_key) # Configure the model
		chat_session = self.start_chat_session(self.model, f"Hi, Gemini.") # Start the chat session
		output = self.send_message(chat_session, task_message) # Send the message

		return output # Return the output

def main():
	"""
	Main entry point to run the GeminiModel.

	:param None
	:return: None
	"""

	print(f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}Gemini AI Model{BackgroundColors.GREEN}!{Style.RESET_ALL}\n\n") # Output the welcome message

	gemini = GeminiModel() # Create the GeminiModel object
	task_message = f"Translate the following text to Portuguese: 'Hello, how are you?'" # The task message
	output = gemini.run(task_message) # Run the GeminiModel
	create_directory(os.path.abspath(OUTPUT_DIRECTORY), OUTPUT_DIRECTORY.replace(".", "")) # Create the output directory
	write_output_to_file(output, GeminiModel.OUTPUT_FILE) # Write the output to the file

	print(f"\n{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}") # Output the end of the program message
	atexit.register(play_sound) # Play a sound when the program finishes

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
