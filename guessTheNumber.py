#This is a number guessing game
#This game comes from an excerisize from the book: "invent your own computer games with python"
#ch4
import random
# imports random number generator as part of the random modules
# there are multiple ways to get a randomized number in python one method is throught the random modules
guessesTaken = 0

print('Hello World, Jk... welcome to the random number game')
print('What is your name?')
name = input()
print('Welcome, ' + name)
print('....')
print()
print()
print()
print('Would you like to play easy ( 5 ), medium ( 4 ) or hard ( 3 )? ( please input the number of guesses )')
guessNum = int(input())
print('I am going to pick a number one through 20, you have ' + str(guessNum) + ' tries to get it right')
gameOn = 0
while gameOn == 0:
    number = random.randint(1, 20)
    guess = 0
    while guessesTaken < guessNum:
        print('What is your guess?')
        guess = int(input())
        guessesTaken = guessesTaken + 1
        if guess > number:
            print('Your guess was too high')
        
        if guess < number:
            print('Your guess was too low')
        
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Congratulations, ' + name + ', you guessed the number in ' + guessesTaken + ' tries!!!')
    
    if guess != number:
        print('Sorry the number I was thinking about was ' + str(number) )
    print('do you want to play again?')
    answer = input('Yes, or No?: ')
    if answer == 'No' or answer == 'no':
        gameOn = 1
        break
    
    else:
        guessesTaken = 0
