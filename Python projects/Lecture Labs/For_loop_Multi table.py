'''
Author: Jimmy Torres
Date: 4/3/2025
CS1030
Program: For Loops Practice

Purpose: In Class work for understanding for loops.
'''
#The following range from 1 to 8 will print. this range is called "i".

#This is for the desired amount of multiplication problems the user wants to see.
user_input = int(input("Please enter the highest number for multiplacation table for the number three"))


#This for loop will print the range based on the user input. Because of the way Pyhthon
#is designed, a +1 value is added to the range to match the user's desired input.
for i in range (1,user_input +1):
    #multi_table variable is added to capture each time the calculation is multiplied.
    multi_table = 3*(i)
    #Every line is calculated until the range is met.
    print(f"3*{i} = {multi_table}")
#End of Program 
    
