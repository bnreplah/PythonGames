#Tic Tac Toe

import random
def drawBoard(board):
    #this function prints out the board that it was passed
    # "board" is a list of 10 things representing the board ( ignore index 0 )
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    #the choices for the game go 

def inputPlayerLetter():
    #let the player type which letter they want to be
    # return a list with the player's letter as the first item, and the computer's letter as the second/
    letter =''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    
    # the first element in the list is the player's, the second is the computer's letter
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False
    print('Do you want to play again? ( yes or no)')
    return input().lower().startswith('y')
    # returns if true if wants to play again

def makeMove(board, letter, move):# doesn't return anything ? makes the move on the board and populates the board array
    board[move] = letter

def isWinner(board, letter):
    #given a board and a player's letter, this function returns True if that player has won
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # accross the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # accross the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # accross the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[2] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter) # diagonal
    )

def getBoardCopy(board):
    # makes a duplicate of the board list and return it the duplicate
    dupeBoard = [] # initializes the array

    for i in board:
        dupeBoard.append(i) # adds to the end of the list
    return dupeBoard # returns the populated list

def isSpaceFree(board, move): # checks to see if the space on the board is free
    # Return true if the passed move is free on the passed board
    return board[move] == ' '

def getPlayerMove(board):
    move = ' ' # initializes the players moves in the function to be passed out of the function
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)): # keeps looping until a valid move is inputed
        print('What is your next move? (1-9)')
        move = input() # queries the users move
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board
    # Returns None if there is no valid move
    possibleMoves = []
    for i in movesList: # loops through every move in the move list
        if isSpaceFree(board, i):
            possibleMoves.append(i)  #appends all possible moves to possibleMoves
        
    if len(possibleMoves) != 0: # if there are any possible moves left
        return random.choice(possibleMoves) # Returns a random choice out of the possible choices available

    else: # if none returns none
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move
    # the AI algorithms
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    
    # Here is our algorithm for our tic tac toe AI:
   
    # First, check if we can win in the next move:
    for i in range(1, 10): # while ranging through the 9 options
        copy = getBoardCopy(board) # gets a copy of the current board
        if isSpaceFree(copy, i): # checks if the space is free ( creating possible / free move list)
            makeMove(copy, computerLetter, i) # makes the move on the copy of the board
            if isWinner(copy, computerLetter): # checks after each move if its a winner
                return i # if we win with the move returns the move
   
    # Checks if the player could win on his next move and blocks him
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i # returns the value needed to block the player if the player were to win with that move
   
    # Tries to take one of the corners if they are free and the past conditions didn't return a value
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None : # returns none if those moves are not available
        return move
   
    # Tries to take the center if it is free
    if isSpaceFree(board, 5):
        return 5
    
    #Moves on one of the sides if no other moves are available
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

# the next functions checks if it's a cats game ( tie or blackout )
def isBoardFull(board):
    #return True if every space on the board has been taken. Otherwise will return false
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

# Now instrumenting putting together the different functions
def play():
    print(' Welcome to tic tac toe! ')

    while True:
        #reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                #player's turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner( theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('HOOORAY! You habe won the game')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie')
                        break
                    else:
                        turn = 'computer'
            else:
                #computer's turn
                move = getComputerMove( theBoard, computerLetter)
                makeMove( theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you.... YOU LOSE')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!!')
                        break
                    else:
                        turn = 'player'
        if not playAgain():
            break


play()