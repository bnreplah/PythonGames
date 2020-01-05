import random

NUMDIGITS = 3
MAXGUESS = 10

def getSecretNum(numDigits):
    # Returns a string that is numDigits long, made up of unique random digits
    numbers = list(range(10))
    random.shuffle(numbers) #shuffles the listso they are more random 
    secretNum = ''
    for i in range(numDigits):
            secretNum += str(numbers[i])
    return secretNum # creates a number with the amount of digits declared in the parameter

def getClues( guess, secretNum ):
    #retruns a string with the pic, ferm, bagels clues to the user
    if guess == secretNum:
        return 'you got it!'
    
    clue = []

    for i in range(len(guess)): # for i in the range of the number of integers in guess
        if guess[i] == secretNum[i]:
            clue.append('Fermi') # if number is right and in irght place
        elif guess[i] in secretNum:
            clue.append('Pico') # if number is right in wrong place
    if len(clue) == 0:
        return 'bagels' #if none of the numbers are right
    
    clue.sort() # sorts in ascending order
    return ' '.join(clue) # returns a single string of the clues given seperated by a space

def isOnlyDigits(num):
    #returns true if the value is only made up of digits
    if num =='':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns false
    print('Do you want to play again? ( yes or no )')
    return input().lower().startswith('y')

#NUMDIGITS = 3
#MAXGUESS = 3
# these are constants as defined by the conventions, hence why they are in all caps, the book places the constants where thye are initialized, It is my practice to place them 
# ~~ at the top of the program

#the book includes this as part of the program, however I am going to make the game play part of a function,
# ~~ in order to possibly use the program in the future in other programs if need be.

def play():
    print('I am thinking of a d %s-digit number. Try to guess what it is.' %(NUMDIGITS)) # %s digit is defined by the %(NUMDIGITS) and is imported into the print statement
    print('Here are some clues:')
    print('When I say:          That means:')
    print(' Pico                One digit is correct but in the wrong position')
    print(' Fermi               One digit is correct and in the right position')
    print(' Bagels              No digit is correct')

    while True:
        secretNum = getSecretNum(NUMDIGITS)
        print('I have thought up a number. You have %s guesses to get it. ' %(MAXGUESS)) #%s in the variable is defined as MAXGUESS    

        numGuesses = 1
        while numGuesses <= MAXGUESS: # while the number of guesses is less than or equal to the number of max guesses
            guess = ''# initializes guess as a blank string
            while len(guess) != NUMDIGITS or not isOnlyDigits(guess): # Begins the loop as the length of the guess is not than the length of the possible number of digits and is not only digits
                #this requires the user to guess and submit a new guess every time they don't meet the requirments of the guess
                print('Guess #%s: ' %(numGuesses)) #%s is defined as the current guess number
                guess = input()# queries the user for input to populate the guess

            clue = getClues(guess, secretNum)
            print(clue)
            numGuesses += 1

            if guess == secretNum:
                break # if the guess is equal to the secret number break the loop and display that the user has won
            if numGuesses > MAXGUESS:
                print('You ran our of guesses. The Answer was %s.' %(secretNum)) #%s defined as the secretnumber displayed if the user was on thier last guess and failed. Displayed before they break the loop

        if not playAgain(): # if play again returns false
            break# break the game play loop
    print('Bye, thank you for playing.')

play()
    