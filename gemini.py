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
	VERBOSE = False # Verbose mode
	ENV_PATH = "./.env" # The path to the .env file
	ENV_VARIABLE = "GEMINI_API_KEY" # The environment variable to load
	OUTPUT_DIRECTORY = "./Outputs/" # The path to the output directory
	OUTPUT_FILE = f"{OUTPUT_DIRECTORY}Gemini_output.txt" # The path to the output file

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
	
	def create_directory(self, full_directory_name, relative_directory_name):
		"""
		Creates a directory.

		:param full_directory_name: Name of the directory to be created.
		:param relative_directory_name: Relative name of the directory for terminal display.
		:return: None
		"""

		self.verbose_output(true_string=f"{BackgroundColors.GREEN}Creating the {relative_directory_name} directory...{Style.RESET_ALL}") # Output the creation message

		if not os.path.isdir(full_directory_name): # If the directory does not exist
			try: # Try to create the directory
				os.makedirs(full_directory_name) # Create the directory
			except OSError: # If an error occurs
				print(f"{BackgroundColors.RED}Creation of the {BackgroundColors.GREEN}{relative_directory_name}{BackgroundColors.RED} directory failed.{Style.RESET_ALL}") # Output the error message

	def configure_model(self, api_key):
		"""
		Configures the Gemini AI model.

		:param api_key: The API key for configuration.
		:return: The configured model.
		"""

		self.verbose_output(true_string=f"{BackgroundColors.GREEN}Configuring the Gemini Model...{Style.RESET_ALL}") # Output the configuration message

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

		self.verbose_output(true_string=f"{BackgroundColors.GREEN}Starting the chat session...{Style.RESET_ALL}") # Output the chat session message

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

		self.verbose_output(true_string=f"{BackgroundColors.GREEN}Sending the message...{Style.RESET_ALL}") # Output the sending message

		output = chat_session.send_message(user_message) # Send the message
		return output.text # Return the output text

	def write_output_to_file(self, output, file_path=OUTPUT_FILE):
		"""
		Writes the chat output to a file.

		:param output: The output text.
		:param file_path: Path to the file.
		:return: None
		"""

		self.verbose_output(true_string=f"{BackgroundColors.GREEN}Writing the output to the file...{Style.RESET_ALL}") # Output the writing message

		with open(file_path, "w") as file: # Open the file
			file.write(output) # Write the output

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
