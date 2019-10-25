#python3
#Topics covered in this exersize
#   the time module
#   time.sleep()
#   defining a function using def
#   TRUTH TABLES
#   and, or, not boolean expressions
#   Variable scope( Global and Local )
#   Parameters and arguments
#   Flow charts
## two functions have already been seen: input() and print(), inside modules are functions, in the parentesis are the parameters of the function. The function print() for example has many defined functions in the built in python library
##      A function is unique and is defined by its paramters and name. That is known as it's signature.
import random
import time
# This program is an adaptation of the DragonRealm game found in the book: invent with python. The books code can be found on inventwithpython.com/chapter6
#   This version is longer and doesn't follow the same signature as the code from the book. It was inspired by the code found in the book.


cont = 1
def displayIntro():
    dragon = random.randint(1,2)
    print('Welcome Brave traveler, you have found your self into the magical world that is known as Dragon\'s Realm. I hope you enjoy your stay. ')
    print('Be warry of the magical creatures which lurk in such a place, for not all of them are friendly, and not all of them are kindhearted')
    print()
    print()
    print('You begin your journey....')
    time.sleep(5)
    print()
    print('After a while, you find yourself presented with two caves, In one cave there is a dangerous sleeping dragon, and in the other are')
    print(' goblins waiting to string you up and eat you')
    return dragon
    
def chooseCave(dragon):
    cave = ''
    while cave != '1' and cave != '2': #making sure that at least one value is inputed. Using Boolean operators
        print('Which cave will you go into? (1 or 2)' )
        cave = input()
        #print(cave)        # debugging purposes
        #print(dragon)
    return (int(cave), int(dragon)) # tuple

def checkCave(chosenCave): # here is breifly introduced the concept of encapsulation by the parameter variable seen 
    cave = chosenCave[0] #assigning the tuple inside the function
    dragon = chosenCave[1]
    cont = 1
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(4)
    print('You hear rumbling, so you lift your light and you see ...', end='') #end= assigns what will proceed instead of a new line after the print statment is done
    time.sleep(4)
    if dragon == cave:
        print(' It\'s a Dragon, but he\'s sleeping, you can sneak on by without stepping on his tail' )
    if dragon != cave:
        print(' ... A band of goblins!!! They tied you up, flip you over, steal all your pocessions, and eat you.')
        cont = 0
    return cont

def sneakBy():
    cont = 1
    print()
    print('You attempt to sneak on by...')
    time.sleep(3)
    luck = random.randint(0,1)
    if luck == 1:
        print(' You succeed to sneak on by...')
        print()
    else:
        print('You stepped on the dragons tail, the dragon awoke..... ')
        print('He stares into your eyes, and you feel his soul peering back at you, slowly he opens his mouth')
        print('He devours you whole')
        print()
        time.sleep(3)
        luck = random.randint(0, 1)
        if luck == 1:
            print('However you survive')
        else:
            print('You perished in his stomach, and that is the end of your tale my friend.')
            cont = 0
    return cont

def survivor():
    cont = 1
    input('... hit enter, to continue ...')
    print()
    print('You are a survivor, on the otherside, you exit the cave and see a land filled with faeries')
    print('You are relieved, for faeries are known to be friendly....', end='')
    time.sleep(3)
    print('SO YOU THOUGHT')
    print()
    print('It really isn\'nt your day adventurer.')
    print('You get attacked by a bunch of fairy warriors')
    print()
    print('Do you fight? (yes, or no)')
    print()
    fight = ''
    while fight != 'yes' and fight != 'no':
        fight = input()
        if fight == 'yes':
            print('You defeat the faeries, and they elect you to be their master')
            print('You live happily ever after as the ruler of the faeries, and spend the rest of your life as the master of the faeries')
        if fight == 'no':
            print('you are defeated and slain in battle')
            cont = 0 
    return cont

def play():
    cont = checkCave(chooseCave(displayIntro()))
    if cont == 1:
       cont = sneakBy()
    if cont == 1:
        #print( str(survivor()) )
        survivor()

playAgain = 'yes'
while playAgain != 'no' and ( playAgain == 'yes' or playAgain == 'y' ) :
    play()
    print('would you like to play again?')
    playAgain = input()

# in the following program, you can see the use of tuples, indexing, and, or , if and while statements as well as the use of the time.sleep() function which waits
# for a certain amount of time to pass. The game randomizes the chances for a player to survive so it won't necessarily be the same correct choices as before
# this short game can be evolved, and in time I may choose to write a longer more adventurous version
# Boolean values fit into a truth table as such ( which dictate how 'and' and 'or' statments work)
#   True and True = True
#   True and False = False
#   False and True = False
#   False and False = False
#   True and True = True

#   True or True = True
#   True or False = True
#   False or True = True
#   False or False = False

# not True = False
# not False = True

# we also see variable scope in this exercise, variables called in the functions are called in the local scope, and variable called outside are in the global scope
# global variables can't be changed inside the local scope but they can be read, and local variables only exist inside the local scope.
# functions can only be called after they are defined, if they are put before they are defined an error is called
# to design a game create a flow chart, with each option creating a branch and the results leading to the end of a game. Somewhat similiar to a cricuit, each option must lead to the end but the journey is the question.