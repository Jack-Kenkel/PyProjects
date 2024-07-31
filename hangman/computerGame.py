# two versions 1 is a two player where the first user
# inputs the word and then second player guesses
# other is computer choses random word and player guesses
import random

def updateWord(matches, currentword, word, lives, letter):
    if len(matches) == 0:
        lives -= 1
        print(f"The word does not contain {letter} :(")
    else:
        temp = list(currentword)
        for index in matches:
            temp[index] = word[index]
            currentword = ''.join(temp)
            print(f"The word does contain {letter}!")
    return currentword, lives

def computerHangman():
    words = open("/Users/jackkenkel/Desktop/PyProjects/hangman/wordlist.10000.txt").read().splitlines()
    word = random.choice(words)
    lives = 9
    currentword = '-' * len(word)
    letters = []

    while lives > 0 and currentword != word:
        print(f"The current word to guess is {currentword}. You have {lives} guesses remaining and have guessed {letters}")
        # add in validation of input
        letter = input("Please guess a letter: ").lower()
        letters.append(letter)
        matches = [index for index, character in enumerate(word.lower()) if letter == character]
        currentword, lives = updateWord(matches, currentword, word, lives, letter)

    if(currentword == word):
        print(f"congratulations you have guessed the word {word}!")
    else:
        print(f"No lives remaining you lost the word was {word}")
    
   
            


computerHangman()