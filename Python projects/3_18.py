'''
Author: Jimmy Torres
CS1030
Last date edited: 3/28/2025
Date created: 3/18/2025

Program: Rock, Paper, Scissors game.

Author note: The following program is not in a linear sequence. The introduction function gets the Player input (playerSel).
The function then gets the computer's selection (computerSel) in the computerturn function. It compares the user input to the
computer input in the rpsgame function. The current version does not have a score keeper or a game counter. The use of the the
several print lines and stars are used to avoid walls of text in this program, and give a visual aid to the user.
'''

#Below here is the random module being called. This will be used to ensure the computer is
#creating random selections.
import random

#This tells the user what the program is for.
print("****************************************************************************")
print("Hello! We're going to play Rock, Paper, Scissors. Can you beat the Computer? \n Lets Find Out!")
#This allows the user to create a username of their liking. The print method verfies the username
#to the user.
playername = input("What username would you like to use? Please enter here:   ")
print(f"Hi {playername}!")

#The introduction function is what the player is introduced to before playing. Every new game starts here.
def introduction():
    #while loop sets condition for a specific string that the the loop is looking for. This is
    # to ensure the user only selects rock paper or scissors.
    while True:
    #The User input will be lowercased to ensure it matches the variables listed. The options are; rock, paper, or scissors.
    #Any other input is caught and the user is notified. to try again.

        #This print line is used to visually identify each new game that starts.
        print("**************************************************************")
        playerSel = input("Type rock, paper, or scissors: ").lower()
        if playerSel in ["rock", "paper", "scissors"]:
            #User is notified of their input.
            print("_______________________________________")
            print(f"{playername} has selected \n{playerSel}.")
            print("_______________________________________")
            #This line of code acts as a buffer before the next function is called for the computer to select a random value.
            input("It's the computer's turn! (Press enter)")
            #computerSel variable does not get calculated here. The function computerturn() is called to calculate the computer's turn.
            computerSel = computerturn()
            #The rpsgame function is called to compare the playerSel variable and the computerSel variable.
            rpsgame(playerSel, computerSel)
            #This line of code will save the user input to be the new variable value. Return is used so that the value can be
            #reused in other functions. This return value MUST be last in this IF loop to work.
            return playerSel
        #The else is any other possible option or typo entered by the user. These are invalid and start the loop over again.
        else:
            print("Whoops, try again!")
            introduction()
#This function will create a random integar value and convert the value to a string (rock, paper, or scissors).
#This function is NOT visible to the user.
def computerturn():
    #using 1 and 3 as arguments, a random integar between the range of 1 to 3 is selected. 
    computerSel = random.randint(1, 3)
    #A value equal to 1 is rock.
    if computerSel == 1:
        return "rock"
    #avalue equal to 2 is paper.
    elif computerSel == 2:
        return "paper"
    #The remaining value of 3 is scissors.
    else:
        return "scissors"
    #The value is returned to be used in the final function.
    return computerSel
    
#This function compares the user input to the computer's value. The two arguments are the returned values in the first two functions.
def rpsgame(playerSel, computerSel):
    #The User is shown the computer's selection from the computerturn function
    print("_______________________________________")
    print(f"The computer picks: \n{computerSel}.")
    print("_______________________________________")
    #This IF loop will determine the game. The first if conditions defines equal values of strings as a draw.
    if playerSel == computerSel:
        print(f"Oh man! You both picked {playerSel}\nIT'S A DRAW!")
        #restart function is called.
        restart()
    #This IF condition lists all possibilities that make a player beat the computer: R > S | P > R | S > P
    elif (playerSel == "rock" and computerSel == "scissors") or (playerSel == "paper" and computerSel == "rock") or (playerSel == "scissors" and computerSel == "paper"):
        print(f"{playerSel} beats {computerSel}! \n{playername} WINS!")
        #Restart function is called.
        restart()
    #All other conditions are computer wins.
    else:
        print(f"{computerSel} beats {playerSel}! \nTHE COMPUTER WINS!")
        #Restart Function is called.
        restart()
#The restart function give the player an opportunity to play again. This structure is similar to the introduction function.
def restart():
    #Player response is requested. All responses are lowercased to ensure uniformity of syntax.
    print("_______________________________________")
    print("Would you like to play again?   Y/N?")
    playerOption = input("Your Response:    ").lower()
    #IF Yes, introduction function is called again. Game restarts. After testing, the break syntax must be in both IF and ELIF to prevent infinite loops.
    while True:
        if playerOption == ("y"):
                  introduction()
                  break
        #IF No, player is instructed to close window. No function is called.
        elif playerOption == ("n"):
                  print(f"Thanks for playing {playername}! Have a Great Day!")
                  print("Close this window to exit the program.")
                  print("****************************************************************************")
                  break
        #All other responses restart this IF loop with the restart function being called again.
        else:
                  print("Whoops! Try again!")
                  restart()
              
#The Introduction function starts the game. All functions are defined before this function.
introduction()

#END OF PROGRAM


    
