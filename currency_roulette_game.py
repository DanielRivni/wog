import random
from currency_converter import CurrencyConverter

# Function that gets the currency rate and the interval
def get_money_interval(difficulty):
    currency = CurrencyConverter().convert(1, 'ILS', 'USD')
    match difficulty:
        case '1':
            interval = 9
        case '2':
            interval = 8
        case '3':
            interval = 7
        case '4':
            interval = 6
        case '5':
            interval = 5
        case _: 
            raise ValueError("Invalid difficulty level. Must be between 1 and 5.")
    

    return interval, currency

# Function that gets the guess from the user
def get_guess_from_user():
    random_number = random.randint(0,100)
    user_input = float(input(f"Please guess the value of {random_number} ILS in USD:\n"))
    return user_input, random_number

# Function that compare between the currency rate and the user guess
def compare_results(difficulty):
    interval, currency = get_money_interval(difficulty)
    user_input, random_number = get_guess_from_user()
    if abs(user_input - (random_number * currency)) <= interval:
        print("Congratulations, you won!")
        return True
    print("Sorry, that's not correct.")
    return False

# Function that runs all the other functions
def play(difficulty):
    if compare_results(difficulty):
        return True
    return False



