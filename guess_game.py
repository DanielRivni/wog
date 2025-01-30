import random

# Function that get a random number bwtween 0 and the difficulty
def generate_number(difficulty):
    return random.randint(0,int(difficulty))

# Function that gets a number from the user
def get_guess_from_user(difficulty):
    user_number = int(input(f"Please choose a number between 0 and {difficulty}:\n"))
    return user_number

# def get_guess_from_user(difficulty):
#     while True:
#         try:
#             user_number = int(input(f"Please choose a number between 0 and {difficulty}:\n"))
#             if 0 <= user_number <= difficulty:
#                 return user_number
#             else:
#                 print(f"The number must be between 0 and {difficulty}. Try again.")
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

# Function that check of the two number are equal
def compare_results(secret_number, user_number):
    if secret_number == user_number:
        print("Congratulations, you won!")
        return True
    print("Sorry, that's not correct.")
    return False

# Function that runs all the other functions    
def play(difficulty):
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    if compare_results(secret_number, user_number):
        return True
    return False

