import atexit # For playing a sound when the program finishes
import os # For running a command in the terminal
import pandas as pd # For reading CSV files
import platform # For getting the operating system name
import sys # For exiting the program
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

# Input Constants:
INPUT_DIRECTORY = "./Inputs/" # The path to the input directory
INPUT_CSV_FILE = f"{INPUT_DIRECTORY}input.csv" # The path to the input CSV file

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

def play_sound():
   """
   Plays a sound when the program finishes.

   :return: None
   """

   if verify_filepath_exists(SOUND_FILE):
      if platform.system() in SOUND_COMMANDS: # If the platform.system() is in the SOUND_COMMANDS dictionary
         os.system(f"{SOUND_COMMANDS[platform.system()]} {SOUND_FILE}")
      else: # If the platform.system() is not in the SOUND_COMMANDS dictionary
         print(f"{BackgroundColors.RED}The {BackgroundColors.CYAN}platform.system(){BackgroundColors.RED} is not in the {BackgroundColors.CYAN}SOUND_COMMANDS dictionary{BackgroundColors.RED}. Please add it!{Style.RESET_ALL}")
   else: # If the sound file does not exist
      print(f"{BackgroundColors.RED}Sound file {BackgroundColors.CYAN}{SOUND_FILE}{BackgroundColors.RED} not found. Make sure the file exists.{Style.RESET_ALL}")

atexit.register(play_sound) # Register the function to play a sound when the program finishes

def read_csv_file():
   """
   Reads tasks from the input CSV file using pandas and returns the DataFrame.

   :return: None
   """

   verbose_output(true_string=f"{BackgroundColors.GREEN}Reading tasks from CSV file using pandas...{Style.RESET_ALL}") # Output the reading message

   if os.path.exists(INPUT_CSV_FILE): # If the input CSV file exists
      df = pd.read_csv(INPUT_CSV_FILE) # Reading the CSV into a DataFrame
      return df # Return the DataFrame
   else: # If the input CSV file does not exist
      print(f"{BackgroundColors.RED}CSV file {BackgroundColors.CYAN}{INPUT_CSV_FILE}{BackgroundColors.RED} not found. Make sure the file exists.{Style.RESET_ALL}")
      sys.exit(1) # Exit the program

def main():
   """
   Main function.

   :return: None
   """

   print(f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}AIs API Response Collector{BackgroundColors.GREEN}!{Style.RESET_ALL}\n\n") # Output the welcome message

   print(f"\n{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}") # Output the end of the program message

if __name__ == "__main__":
   """
   This is the standard boilerplate that calls the main() function.

   :return: None
   """

   main() # Call the main function
