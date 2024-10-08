import google.generativeai as genai # Import the Google AI Python SDK
import os # For running a command in the terminal
import sys # For exiting the program
from colorama import Style # For coloring the terminal
from dotenv import load_dotenv # For loading .env files
from main import BackgroundColors # Import Classes from ./main.py
from main import OUTPUT_DIRECTORY # Import Constants from ./main.py
from main import create_directory, verbose_output, verify_filepath_exists # Import Functions from ./main.py

class GeminiModel:
	"""
	A class to interact with the Google Gemini AI model.

	"""

	# Constants:
	ENV_PATH = "./.env" # The path to the .env file
	ENV_VARIABLE = "GEMINI_API_KEY" # The environment variable to load
	OUTPUT_FILE = f"{OUTPUT_DIRECTORY}Gemini_output.txt" # The path to the output file

	def __init__(self): # Constructor
		self.api_key = None # The API key
		self.model = None # The AI model

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
			model_name="gemini-1.5-flash", # Model name
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

	def write_output_to_file(self, output, file_path=OUTPUT_FILE):
		"""
		Writes the chat output to a file.

		:param output: The output text.
		:param file_path: Path to the file.
		:return: None
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Writing the output to the file...{Style.RESET_ALL}") # Output the writing message

		with open(file_path, "w") as file: # Open the file
			file.write(output) # Write the output

	def run(self, task_message):
		"""
		Main function to run the AI model to do what is described in the task message.

		:param task_message: The message to send to the AI model.
		:return: None
		"""

		self.api_key = self.verify_env_file(self.ENV_PATH, self.ENV_VARIABLE) # Verify the .env file and load API key

		create_directory(os.path.abspath(OUTPUT_DIRECTORY), OUTPUT_DIRECTORY.replace(".", "")) # Create the output directory

		self.model = self.configure_model(self.api_key) # Configure the model

		chat_session = self.start_chat_session(self.model, f"Hi, Gemini.") # Start the chat session
		output = self.send_message(chat_session, task_message) # Send the message

		self.write_output_to_file(output) # Write the output

		return output # Return the output

def main():
	"""
	Main entry point to run the GeminiModel.

	:param None
	:return: None
	"""

	gemini = GeminiModel() # Create the GeminiModel object
	gemini.run() # Run the GeminiModel

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
