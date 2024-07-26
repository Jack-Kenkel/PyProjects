# computer generates a number
# User inputs a number untill guess corretly
# output is higher / lower correct
import random

# guess a number between 0 and x
def guess(x):
    targetNum = random.randint(0, x)
    guesses = 0
    initialGuess = None
    while initialGuess != targetNum:
        # add a validation here
        initialGuess = int(input(f"Guess the secret number between 0 and {x}: "))
        if initialGuess > targetNum:
            print(f"Your guess of {initialGuess} is greater than the secret number. Guess again")
        elif initialGuess < targetNum:
            print(f"Your guess of {initialGuess} is smaller than the secret number. Guess again")
        guesses += 1
    print(f"Congratulations you guessed the secret number {targetNum}! It took you {guesses} guesses")

guess(10)

def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "C":
        if low != high:
            guess = random.randint(low, high) # error if low == high in randint
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), to low (L), or correct (C)??").upper()
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
    print(f"Computer guessed your number, {guess}")

 
