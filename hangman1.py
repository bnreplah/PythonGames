import random
HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # This function returns a random string form the passed list of strings
    wordIndex = random.randint( 0, len(wordList) - 1)
    # indexes all the words in the word list and picks a random umber out fo the index to return
    return wordList[wordIndex]

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord ):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    #print(secretWord) #comment out used for debugging and testing

    for i in range(len(secretWord)):#replaces blanks with correct with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks: # show the secret word with the spaces in between each letter
        print( letter, end= ' ')
    print()

def getGuess(alreadyGuessed):
    #returns the letter the player entered. This function makes sure the plater entered a single letter
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower() # makes them to uncapitalized
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain(): #this function returns True if the player wants to play again, otherwise it returns false
    print('Do you want to play again? ( yes or no )')
    return input().lower().startswith('y')

print('H  A  N  G  M  A  N')
missedLetters = ''
correctLetters =''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    # let the player type in a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('YES! the secret word is "' + secretWord + '" You have Won!!')
            gameIsDone = True
    elif guess not in secretWord:
        missedLetters = missedLetters + guess

            # check if player has guessed too many times and has lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses \nAfter ' + str(len(missedLetters)) + ' missed Guesses and ' + str(len(correctLetters)) + ' correct guesses. \nThe word was "' + secretWord + '"')
            gameIsDone = True

            # ask if the player wants to play again
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break 