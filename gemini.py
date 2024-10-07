import google.generativeai as genai # Import the Google AI Python SDK
import os # For running a command in the terminal
import sys # For exiting the program
from colorama import Style # For coloring the terminal
from dotenv import load_dotenv # For loading .env files

class BackgroundColors: # Colors for the terminal
   CYAN = "\033[96m" # Cyan
   GREEN = "\033[92m" # Green
   YELLOW = "\033[93m" # Yellow
   RED = "\033[91m" # Red
   BOLD = "\033[1m" # Bold
   UNDERLINE = "\033[4m" # Underline
   CLEAR_TERMINAL = "\033[H\033[J" # Clear the terminal

class GeminiModel:
	"""
	A class to interact with the Google Gemini AI model.

	"""

	# Constants:
	ENV_PATH = "./.env" # The path to the .env file
	ENV_VARIABLE = "GEMINI_API_KEY" # The environment variable to load

	def __init__(self): # Constructor
		self.api_key = None # The API key
		self.model = None # The AI model

	def verbose_output(self, true_string="", false_string=""):
		"""
		Outputs a message if the VERBOSE constant is set to True.

		:param true_string: The string to be outputted if VERBOSE is True.
		:param false_string: The string to be outputted if VERBOSE is False.
		:return: None
		"""

		if self.VERBOSE and true_string != "": # If VERBOSE is True and the true_string is not empty
			print(true_string) # Output the true_string
		elif false_string != "": # If the false_string is not empty
			print(false_string) # Output the false_string

	def verify_env_file(self, env_path=ENV_PATH, key=ENV_VARIABLE):
		"""
		Verify if the .env file exists and if the desired key is present.

		:param env_path: Path to the .env file.
		:param key: The key to get in the .env file.
		:return: The value of the key if it exists.
		"""

		self.verbose_output(true_string=f"{BackgroundColors.GREEN}Verifying the .env file...{Style.RESET_ALL}") # Output the verification message

		if not os.path.exists(env_path): # If the .env file does not exist
			print(f"{BackgroundColors.RED}.env file not found at {BackgroundColors.CYAN}{env_path}{Style.RESET_ALL}") # Output the error message
			sys.exit(1) # Exit the program

		load_dotenv(env_path) # Load the .env file
		api_key = os.getenv(key) # Get the value of the key

		if not api_key: # If the key does not exist
			print(f"{BackgroundColors.RED}Key {BackgroundColors.CYAN}{key}{BackgroundColors.RED} not found in .env file.{Style.RESET_ALL}") # Output the error message
			sys.exit(1) # Exit the program

		return api_key # Return the API key

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
