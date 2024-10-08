import atexit # For playing a sound when the program finishes
import os # For running a command in the termina
from colorama import Style # For coloring the terminal
from utils import BackgroundColors # Import Classes from ./utils.py
from utils import OUTPUT_DIRECTORY # Import Constants from ./utils.py
from utils import create_directory, play_sound, verbose_output, write_output_to_file # Import Functions from ./utils.py

class CopilotModel:
	"""
	A class to interact with the Microsoft Copilot AI model.

	"""

	# Constants:

	OUTPUT_FILE = f"{OUTPUT_DIRECTORY}Copilot_output.txt" # The path to the output file

	def __init__(self): # Constructor
		pass # Do nothing

	def explain_command(self, command):
		"""
		Request Copilot to explain a command via GitHub CLI.

		:param command: The command to be explained.
		:return output: The explanation of the command from Copilot.
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Requesting explanation for: {BackgroundColors.CYAN}{command}{Style.RESET_ALL}") # Output the verbose message
		os.system(f"gh copilot explain \"{command}\" > {self.OUTPUT_FILE}") # Run the Copilot CLI command
		with open(self.OUTPUT_FILE, "r") as file: # Open the output file
			output = file.read() # Read the output
		return output # Return the output

	def suggest_command(self, description):
		"""
		Request Copilot to suggest a command based on a description via GitHub CLI.

		:param description: A short description of what you want to achieve.
		:return output: The suggested command from Copilot.
		"""

		verbose_output(true_string=f"{BackgroundColors.GREEN}Requesting command suggestion for: {BackgroundColors.CYAN}{description}{Style.RESET_ALL}") # Output the verbose message
		os.system(f"gh copilot suggest \"{description}\" > {self.OUTPUT_FILE}") # Run the Copilot CLI command
		with open(self.OUTPUT_FILE, "r") as file: # Open the output file
			output = file.read() # Read the output
		return output # Return the output

	def run(self, task_message, task_type="explain"):
		"""
		Main function to run the Copilot CLI to explain or suggest a command.

		:param task_message: The command to be explained or description of what you want.
		:param task_type: Type of task, either "explain" or "suggest".
		:return output: The output from Copilot.
		"""
	
		if task_type == "explain": # If the task type is "explain"
			return self.explain_command(task_message) # Return the explanation of the command
		elif task_type == "suggest": # If the task type is "suggest"
			return self.suggest_command(task_message) # Return the suggested command
		else: # If the task type is invalid
			raise ValueError(f"Invalid task_type: {task_type}. Use 'explain' or 'suggest'.") # Raise a ValueError

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
