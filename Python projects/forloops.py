'''
Author: Jimmy Torres
Date: 4/3/2025
CS1030
Program: For Loops Practice

Purpose: In Class work for understanding for loops.
'''


userinputs = []

def input_function():

    while True:
        userinput = input("Please enter an input to save, type 'done' when you are finished")

        if userinput == "done":
            break
        else:
            userinputs.append(userinput)
    
input_function()

for userinput in userinputs:
    print (userinput)

