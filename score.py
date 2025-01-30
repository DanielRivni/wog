from utils import SCORES_FILE_NAME


def reset_score():
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write("0")  # Reset score to 0


def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME, 'r+') as file: 
            content = file.read().strip()
            if not content.isdigit(): 
                content = "0"
            current_score = int(content)
            print("File read successfully.")
    except (FileNotFoundError, IOError):
        print(f"File '{SCORES_FILE_NAME}' not found. Creating a new one.")
        current_score = 0

    new_score = str (current_score + (int(difficulty) * 3) + 5)  

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_score))

    return new_score