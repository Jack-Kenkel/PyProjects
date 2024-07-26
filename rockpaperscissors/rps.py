# user selects r, p, or s output is win or lose depending on randomly 
# selected computer play
import random

# return true if computer wins
def isComputerWin(userMove, computerMove):
    if userMove == "R" and computerMove == "P" \
          or userMove == "P" and computerMove == "S" \
          or userMove == "S" and computerMove == "R":
            return True
    else: 
        return False

def rps():
    userMove = input("Enter S for scissors, R for rock or P for paper- ").upper()
    computerMove = random.choice(["R","P","S"])
    while userMove == computerMove:
        print(f"Computer plays {computerMove}")
        userMove = input("It is a draw!! Chose rock (R) Paper(P) or Scissor (S) again!- ").upper()
        computerMove = random.choice(["R","P","S"])

    print(f"Computer plays {computerMove}")

    if isComputerWin(userMove, computerMove):
        print("Computer wins :(")
    else:
        print("You win!!!")

rps()