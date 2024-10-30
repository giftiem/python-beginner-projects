"""
Create a game that sums the faces of simulated throws of a random 
amount of dice. 
Then gets the user to guess the sum of the die five times, given 
the number of dice that were thrown.
Print whether their guess was too high, low, or exact.

"""

import random

def dice_sum(number_of_dice):
    """
    Write a function that sums the faces of a random number of 
    die between 1 and 10.
    """
    dice_sum = 0
    for _ in range(number_of_dice):
        number = random.randint(1,6)
        dice_sum += number

    return dice_sum

def correct_guess(dice_sum, guess):
    """
    Write a function that returns whether the guess was too high,
    too low, or exact.
    """
    if guess == dice_sum:
        print("Correct!")
        return True
    elif guess > dice_sum:
        print("Your guess was too high!")
        return False
    else:
        print("Your guess was too low!")
        return False

def guessing_game(number_of_guesses):
    counter = 0
    guess = 0
    number_of_dice = random.randint(1,10)
    sum_die = dice_sum(number_of_dice)

    while (counter < number_of_guesses) and (guess != sum_die):
        guess = input(f"Guess the sum of {number_of_dice} dice: ")
        while not guess.isdigit():
            print("Please enter a number!")
            guess = input(f"Guess the sum of {number_of_dice} dice: ")
        
        guess = int(guess)
        correct_guess(sum_die, guess)
    
    print(f"The answer was {sum_die}")

guessing_game(5)

