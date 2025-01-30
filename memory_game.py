import random
import ast
import time
import os

# Function that generate the numbers that the user will need to remember
def generate_sequence(difficulty):
    random_numbers = []
    for _ in range(int(difficulty)):
        random_numbers.append(random.randint(1, 101))
    print (random_numbers)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    return random_numbers

# List of numbers that the user input
def get_list_from_user(length):
    user_numbers = {}
    user_numbers = input(f"Please input a list of numbers that is maching the length {length} (e.g., [1, 2, 3, 4]):\n")
    user_list = ast.literal_eval(user_numbers)
    return user_list

# Function that check if the two list matches
def is_list_equal(difficulty):
    random_numbers = generate_sequence(difficulty)
    user_list = get_list_from_user(len(random_numbers))
    if random_numbers == user_list:
        print("Congratulations, you won!")
        return True
    print("Sorry, that's not correct.")
    return False

# Play function that runs all thee other functions
def play(difficulty):
    if is_list_equal(difficulty):
        return True
    return False
    
