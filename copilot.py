import os # For running a command in the termina
from utils import OUTPUT_DIRECTORY # Import Constants from ./utils.py
from utils import create_directory, write_output_to_file # Import Functions from ./utils.py

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

	copilot = CopilotModel() # Create the CopilotModel object
	output = copilot.run() # Run the CopilotModel
	create_directory(os.path.abspath(OUTPUT_DIRECTORY), OUTPUT_DIRECTORY.replace(".", "")) # Create the output directory
	write_output_to_file(output, CopilotModel.OUTPUT_FILE) # Write the output to the file

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
