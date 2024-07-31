# tic tac toe against random computer
# user inputs move from available moves
# computer plays move
# board updates after each turn
# to do add options for player vs player
# computer vs computer
import random


## returns W if winner, returns T if Tie, returns "P" if still moves left
def checkStatus(board):
    # check if win
    # win conditions [0,1,2], [3,4,5], [6,7,8] [0,3,6] [1,4,7] [2,5,8], [0,4,8] [2,4,6]
    if board[0] == board[1] and board[1] == board[2] or board[3] == board[4] and board[4] == board[5] \
    or board[6] == board[7]  and board[7] == board[8] or board[0] == board[3] and board[3 ]== board[6] \
    or board[1] == board[4] and board[1] == board[7] or board[2] == board[5] and board[5] == board[8] \
    or board[0] == board[4] and board[4] == board[8] or board[2] == board[4] and board[4] == board[6]:
        return "W"
    elif board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 \
    and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 \
    and board[8] != 8:
        return "T"
    else:
        return "P"

def playerMove(board, playerXTurn):
    print("------------")
    print("")
    status = checkStatus(board)
    if status == "W":
        return "Computer wins"
    elif status == "T":
        return "It's a tie"
    
    move = int(input("Player's (X) turn. Input move (0-8): "))
    while True:
        if  move >= 0 and move <= 8 and board[move] != "X" and board[move] != "O":
            board[move] = "X"
            return "" 
        else:
            move = int(input("Please input a valid move between 0-8 that is untaken"))

def computerMove(board):
    print("------------")
    print("")
    status = checkStatus(board)
    if status == "W":
        return "Player wins"
    elif status == "T":
        return "It's a tie"
    remainingOptions = [position for position in board if position != "X" and position != "O"]
    move = random.choice(remainingOptions)
    board[move] = "O"
    return ""

def printBoard(board):
    print("%s | %s | %s" %(board[0], board[1], board[2]))
    print("%s | %s | %s" %(board[3], board[4], board[5]))
    print("%s | %s | %s" %(board[6], board[7], board[8]))
    



def playVsComp():
    board = [0,1,2,3,4,5,6,7,8]
    printBoard(board)
    status = playerMove(board)
    playerTurn = False
    while status == "":
        printBoard(board)
        if playerTurn == False:
            status = computerMove(board)
            playerTurn = True
        else:
            status = playerMove(board)
            playerTurn = False

    print(status)

# to do
def playVsPlayer():
    board = [0,1,2,3,4,5,6,7,8]
    printBoard(board)
    status = playerMove(board)
    playerXTurn = False
    while status == "":
        printBoard(board)
        if playerTurn == False:
            status = computerMove(board)
            playerTurn = True
        else:
            status = playerMove(board)
            playerTurn = False

    if status == "It's a tie":
        print(status)
    

    


playVsComp()