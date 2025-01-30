import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "404"

# Clears the console screen
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
