import random #imported for the use of randint to pick a random word each time
#HANGMANPICS is a constant vairble thus it's in all caps
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
#the split method splits the string into an array of words seperating them by the spaces
def getRandomWord(wordList):
    # This function returns a random string form the passed list of strings
    wordIndex = random.randint( 0, len(wordList) - 1)
    # indexes all the words in the word list and picks a random number out of the index to return
    return wordList[wordIndex]

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord ): #displays the board of the ascii art, the missed letter, the correct letters
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    print(secretWord) #comment out used for debugging and testing

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
## below is the game being run 
def play(): #this doesn't need to be put in a function, but i put it in a function for the sake of encapsulation and abstraction. Allowing me to run more thigns with the action fo the game being played
    print('H  A  N  G  M  A  N')
    missedLetters = ''
    correctLetters =''
    secretWord = getRandomWord(words)
    gameIsDone = False

    while True: # a loop to keep playing until the player chooses to no longer play, and to loop through the guesses until out of guesses
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
        elif guess not in secretWord: # the in statment checks if the guess is inside or found in the word or variable
            missedLetters = missedLetters + guess

                # check if player has guessed too many times and has lost
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print('You have run out of guesses \nAfter ' + str(len(missedLetters)) + ' missed Guesses and ' + str(len(correctLetters)) + ' correct guesses. \nThe word was "' + secretWord + '"')
                gameIsDone = True

                # ask if the player wants to play again
        if gameIsDone: # if true
            if playAgain():# resets all the variables for a new loop
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break 
play()
# not the best practive to break loops with break, usually its best to use the rule set at the top to break it conditionally 
# can add different variations to the game by allowing players to add or reverse the word list or reverse the hangmanpics
#obj.reverse() obj.append() 
#reverse() reverses the order of the list
#append() adds the value to the end 
#these are list methods, and recall methods are specific to the object type
#methods are like functions but only can be called by object types of their designated class
