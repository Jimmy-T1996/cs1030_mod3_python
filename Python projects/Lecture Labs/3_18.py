
import random

playerSelection = []

playerSelection = input("type rock, paper, scissors")

print(f"The player has selected {playerSelection}.")



def rpsgame():
    print(f"The computer picks {computerSel}")
    if playerSelection == "rock" and computerSel == "rock" or playerSelection == "scissors" and computerSel == "scissors" or playerSelection == "paper" and computerSel == "paper":
        print("its a draw!")
    elif playerSelection == "rock" and computerSel == "scissors" or ("paper" and computerSel == "rock") or "scissors" and computerSel == "paper":
        print("Player 1 wins!")
    else:
        print("Computer wins!")
computerSel = random.randint(1,3)

if computerSel == 1:
    computerSel = "rock"
elif computerSel == 2:
        computerSel = "paper"
else:
        computerSel = "scissors"

rpsgame()

    
