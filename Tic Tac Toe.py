#This is a simple python program which allows users to play Tic tac toe.

#----Global Variables---

#Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"
        ]
#Check if game is still in-progress
gameStillGoing = True

#Who Won or tie?
winner = None

#Who's turn it is
currentPlayer = 'X';

def displayBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
    #display the initial board
    displayBoard()
    while gameStillGoing:
        #Handle the single turn for each player
        handleTurn(currentPlayer)
        #Check if the game is already ended
        checkIfGameOver()
        #Flip to other player
        flipPlayer()
        #the game has ended
    if winner == 'X' or winner == 'O':
        print('Hurry Winner is : ', winner)
    elif winner == None:
        print('It is a Tie')

#Handle the single turn for each player
def handleTurn(currentPlayer):
    print('Its a turn of Player: ',currentPlayer)
    position = int(input('Choose a position from 1 to 9 : '))-1;
    if position < 0 or position > 8:
        print('Invalid input')
        handleTurn(currentPlayer)
    else:
        if board[position] != "-":
            print('Its already taken, Please try again');
            handleTurn(currentPlayer)
        else:
            board[position] = currentPlayer
            displayBoard()

#Check if the game is already ended
def checkIfGameOver():
    checkforWinner()
    checkIfTie()

def checkforWinner():
    #Check if there was a winner based on Row, Column or Diagonal
    rowWinner = checkRows()
    columnWinner = checkColumns()
    diagonalWinner = checkDiagonals()

    global winner

    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        #there was no winner
        winner = None

    return

def checkRows():
    global gameStillGoing
    #Check any of the rows have same value and not empty
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        gameStillGoing = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def checkColumns():
    global gameStillGoing
    # Check any of the rows have same value and not empty
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        gameStillGoing = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def checkDiagonals():
    global gameStillGoing
    # Check any of the rows have same value and not empty
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        gameStillGoing = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return

def checkIfTie():
    global gameStillGoing
    if "-" not in board:
        gameStillGoing = False
    return

#Flip to other player
def flipPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return

play_game()