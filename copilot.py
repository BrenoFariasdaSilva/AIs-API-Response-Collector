import atexit # For playing a sound when the program finishes
import os # For running a command in the termina
from colorama import Style # For coloring the terminal
from utils import BackgroundColors # Import Classes from ./utils.py
from utils import OUTPUT_DIRECTORY # Import Constants from ./utils.py
from utils import create_directory, play_sound, write_output_to_file # Import Functions from ./utils.py

class CopilotModel:
	"""
	A class to interact with the Microsoft Copilot AI model.

	"""

	# Constants:

	OUTPUT_FILE = f"{OUTPUT_DIRECTORY}Copilot_output.txt" # The path to the output file

	def __init__(self): # Constructor
		pass # Do nothing

	def run(self, task_message):
		"""
		Main function to run the AI model to do what is described in the task message.

		:param task_message: The message to send to the AI model.
		:return output: The output text.
		"""

		pass # Do nothing

def main():
	"""
	Main entry point to run the CopilotModel.

	:param None
	:return: None
	"""

	print(f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}GitHub Copilot AI Model{BackgroundColors.GREEN}!{Style.RESET_ALL}\n\n") # Output the welcome message

	copilot = CopilotModel() # Create the CopilotModel object
	task_message = "Explain how to create a new branch in Git." # The task message
	task_type = "explain" # The task type
	output = copilot.run(task_message, task_type) # Run the CopilotModel
	create_directory(os.path.abspath(OUTPUT_DIRECTORY), OUTPUT_DIRECTORY.replace(".", "")) # Create the output directory
	write_output_to_file(output, CopilotModel.OUTPUT_FILE) # Write the output to the file

	print(f"\n{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}") # Output the end of the program message
	atexit.register(play_sound) # Register the function to play a sound when the program finishes

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
