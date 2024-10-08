import os # For running a command in the terminal
import platform # For getting the operating system name
from colorama import Style # For coloring the terminal

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

# File Path Constants:
START_PATH = os.getcwd() # The starting path

# Input/Output Directory Constants:
OUTPUT_DIRECTORY = f"{START_PATH}/Outputs/" # The path to the output directory

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

def write_output_to_file(output, file_path):
   """
   Writes the chat output to a file.

   :param output: The output text.
   :param file_path: Path to the file.
   :return: None
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Writing the output to the file...{Style.RESET_ALL}") # Output the writing message

   with open(file_path, "w") as file: # Open the file
      file.write(output) # Write the output

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

   print(f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}Utils{BackgroundColors.GREEN} program!{Style.RESET_ALL}") # Output the welcome message
   print(f"{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}") # Output the end of the program message

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
