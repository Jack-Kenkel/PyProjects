# user enters secret number and computer tries to guess it
# user gives feedback either low or high
import random

def guess(secretNumber):
    guesses = 0
    currentGuess = None
    minGuess = 0
    maxGuess = 1000
    while(currentGuess != secretNumber):
        currentGuess = random.randint(minGuess, maxGuess)
        status = input(f"is the secret number higher (H) lower (L) or equal (C) to {currentGuess}: ")
        if status == "H":
            minGuess = currentGuess
        elif status == "L":
            maxGuess = currentGuess
        guesses += 1
    print(f"Your secret number is {currentGuess}. It took {guesses} to guess.")
    



def main():
    secretNumber = input("Please enter a secret integer number between 0 and 1000: ")
    guess(int(secretNumber))


main()






