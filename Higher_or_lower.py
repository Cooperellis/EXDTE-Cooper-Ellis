# Imports the ability to have random number
import random
guess = 0
trys = 0
add_trys = 1
# Prints welcome to the game and starts when user presses enter
print("Welcome to Higher or lower a game of guessing numbers.")
start = input("Press enter to start ")

#picks random number
number = random.randint(1, 100)

#if the guess is lower or higher than the number it will rerun that section
while guess > number or guess < number:
        
    #takes user guess
    guess = int(input("Guess a number from 1 to 100 "))

    if guess == number:
        print("Congratulations! You guessed the number!")
    elif guess < number:
        print("Higher")
        trys += add_trys
    else:
        print("Lower")
        trys += add_trys
    if trys > 9:
        print("Sorry, You only get 10 trys. ")