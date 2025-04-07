'''
Author: Jimmy Torres
Date: 4/1/2025
Program: Guess number game

Note: This game will prompt the user to guess the correct number generated
by the computer until they get it right.
'''
#This imports the random module/library 
import random

#This variable is calculated using the random module. Randint will pull a
# random integar between 0 and 100 (argument).
number = random.randint(0,100)

# This print method is the first line of information presented to the user.
print("Guess the magic number between 0 and 100")

#The value of -1 is just a placeholder until values in the range is added.
guess = -1

# This while loop will tell the user if their number is too low, high or the actual number.
# It will repeat until the conditions
# make the user have an equal number.
while guess != number:
    #User input
    guess=int(input("\nEnter your guess:"))
    #Equal condition
    if guess == number:
        print(f"Yes, the number is {number}!!!")
    #guess is too high condition
    elif guess>number:
        print("Your guess is too high")
    #guess is too low condition
    else:
        print("Your guess is too low!")
        
#END OF PROGRAM
