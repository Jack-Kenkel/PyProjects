# two versions 1 is a two player where the first user
# inputs the word and then second player guesses
# other is computer choses random word and player guesses

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

def twoPlayerHangman():
    word = input("Player 1 please enter a word (don't show player two who will be guessing the word): ")
    # guess while still have chances left or until guessed word matches word
    lives = 9
    currentword = word
    for x in currentword:
        if(x != " "):
            currentword = currentword.replace(x, '-')
    # more efficient way but doesn't handle spaces
    # currentword = '-' * len(word)
    letters = []
    while lives > 0 and currentword != word:
        print(f"You have {lives} attempts remaining \
currently guessed word is {currentword} you have used these letters: {letters}")
        letter = input("Guess a letter: ").lower()
        letters.append(letter)
        # list comprehension
        matches = [index for index, character in enumerate(word.lower()) if character == letter]
        currentword, lives = updateWord(matches, currentword, word, lives, letter)
    if(currentword == word):
        print(f"congratulations you have guessed the word {word}!")
    else:
        print(f"No lives remaining you lost the word was {word}")
    
            


twoPlayerHangman()