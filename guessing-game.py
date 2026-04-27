# This is my final project for python programming. This project will feature a guessing game
# All instructions are provided in the rubric, too many to write in comments here

# Import the random module to generate a random number between the bounds provided by the user
import random

# In order to restart the game, we can call the function
def bounds_and_digit():
    try:
        # Ask the user for the lower and upper bounds
        lower_str = input("Enter the lower bound: ")
        upper_str = input("Enter the upper bound: ")
        # Store values in new variables as integers
        lower = int(lower_str)
        upper = int(upper_str)
        # Raise a value error if the lower bound is greater than the upper bound
        if lower >= upper:
            raise ValueError("Lower bound must be less than upper bound.")
        print("======================================================")
    except ValueError:
        print("Invalid input. Please enter valid integers, and ensure lower bound is less than upper bound.")
        return bounds_and_digit()
    
    # Pick a number between the lower and upper bounds
    picked_digit = random.randint(lower, upper)
    # CALL FUNCTION
    get_guess(picked_digit)

# Try to get the user to guess the number
def get_guess(digit): 
    guessed = False
    attempts = 0

    # Run loop as long as the user hasn't guessed the number
    while guessed == False:
        try:
            guess = int(input("Guess a number in the given range: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if guess == digit:
            guessed = True
            attempts += 1
            print("Congratulations! You guessed the number.")
            break
        elif guess < digit:
            print("Too low! Try again.")
            attempts += 1
            continue
        else:
            print("Too high! Try again.")
            attempts += 1
            continue
    # Print formatted message with attempts and ask if they want to play again
    print("=======================================================")
    print(f"It took you {attempts} attempts to guess the number.")
    print("Thank you for playing the guessing game!\nWould you like to play again? (yes/no)")
    play_again = input().lower()
    if play_again == "yes":
        # Restart the game
        print("Great! Let's play again.")
        bounds_and_digit()
    else:
        # Goodbye!
        print("Thanks for playing! Goodbye!")
        print("=======================================================")

# Display a welcome message before the game starts
def welcome_message():
    # Prints when the program starts
    print("=======================================================")
    print("Welcome to the Guessing Game!")
    print("In this game, you will be asked to guess a number in a given range")
    print("You will get to decide the range that the number is within")
    print("After each guess, you will be told if your guess is too high, too low, or correct")
    print("Good luck, and have fun playing!")
    print("=======================================================")

if __name__ == "__main__":
    # Call the welcome message and then play the game
    welcome_message()
    bounds_and_digit()