import memory_game
import guess_game
import currency_roulette_game
from score import add_score,reset_score

# A welcome function
def welcome():
    user_name = input("Please enter your Username ")
    print(f"Hi {user_name} and welcome to the World of Games: The Epic Journey")
    reset_score()
    

# Play function that gets the game that the user want to play
def start_play():
    while True:
        print("Please choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
        print("2. Guess Game - guess a number and see if you chose like the computer")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
        print("4. Exit")

        game = input()
        if game == '4':
            print("Thanks for playing! 👋")
            break  

        difficulty = input("Please choose a difficulty level between 1 and 5\n")
        match game:
            case '1':
                if memory_game.play(difficulty):
                    add_score(difficulty)  
            case '2':
                if guess_game.play(difficulty):
                    add_score(difficulty)
            case '3':
                if currency_roulette_game.play(difficulty):
                    add_score(difficulty)
            case default:
                print("Invalid game choice. Please choose a game from the list.")


