'''
Author: Jimmy Torres
Date: 4/3/2025
CS1030
Program: For Loops Practice

Purpose: In Class work for understanding for loops.
'''

#This stores a list
userinputs = []

#This function saves inputs to the userinputs list.
def input_function():
    #While true starts a loop while boolean is implemented.
    while True:
        #This takes inputs by the user.
        userinput = input("Please enter an input to save, type 'done' when you are finished:\n")
        #This stops the loop.
        if userinput == "done":
            break
        #This adds all userinput values that are not 'done' to the userinputs list.
        else:
            userinputs.append(userinput)
#This starts the function when program is started.    
input_function()

for userinput in userinputs:
    print(f"{userinput}")

