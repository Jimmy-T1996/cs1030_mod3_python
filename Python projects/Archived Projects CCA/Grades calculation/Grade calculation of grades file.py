"""
Name of Program: FinalChallenge.py
Author: Jaime Torres
Last Date modified: 8/3/2024

Purpose: The purpose of this program is to calculate the Average, Median, Mode, Largest Integer and smallest Integer
using different functions. The data used will be from an imported file specific to exam grades. The file 'grades.txt'
is required for this program to function and the user will see this at the main menu befor any function is called.
"""


#The main function is displayed here. The main menu is in the main and will be the 'center' for which all functions are called.
def main():
    #Examgrades are listed as a global variable. this is necessary as this will be used by several functions outside of the main().
    global examgrades
    #Exam grades will be a user input. The "input" is them being read by the program, as the values can change the external file.
    examgrades = []

    #The grades.text has the integer information that will be used to be calculated by this program.
    with open('grades.txt', 'r') as file: #With open - will allow the file to be read without needing to be closed.
        #With th above line using 'r' to read, the below line of code will convert the string information to be split and converted
        #to integer numbers for math calculations.
        examgrades = [int(num) for num in file.readline().strip().split()]

    #Below is the header and information that the user will use in the menu for the program. This will use a 'while' loop
    #to ensure only the options provided are used.
    while True:
        #This explains the program to the user.
        print("***Please ensure grades.txt is in the same directory as this program***")#The grades.txt is essential to the function of this program and the user is let known.
        print("The following program, FINAL CHALLENGE will calculate the following:\nAverage, Median, Mode, Largest Integer/grade and Smallest Integer/grade. \nLook at the menu below.")#This reminds the user of the menu options.
        print("-----------------------------------------------")#This is aesthetic.
        #This explains the program options. 
        userinput = input("Please type and enter an option to view the output:\n 1.)Average\n 2.)Median\n 3.)Mode\n 4.)Largest Integer\n 5.)Smallest Integer\n 6.)Exit\nYour Option:")
        #The following reflects all six options to the user. 
        if userinput == "1":
            print("***The grade Average is:", avgfun()) #This calls the function that will find the average when '1' is entered.
        elif userinput == "2":
            print("***The Grade Median is:", medianfun())#This calles the median/middle function when '2' is entered.
        elif userinput == "3":
            print("***The mode of the Grades are:", modefun())#This calls the mode function when '3' is entered.
        elif userinput == "4":
            print("***The largest integer/highest Grade is:", largestfun()) #This calls the largest grade function when '4' is entered.
        elif userinput == "5":
            print("***The smallest integer/Lowest Grade is:", smallestfun())#This calls the smallest grade function when '5' is entered.
        elif userinput == "6":
            print("***Exiting the program.") #'6' will break the loop and therfore end the program.
            break
        else: #Any input not already listed falls into 'else' for invalid inputs. A message will be prompted for correction.
            print("***************************************************")
            print("INVALID INPUT. Please enter an integer from 1 to 6.")#The lines of stars is to ensure the user easily sees the invalid input message. message
            print("***************************************************")

#This is the average function.
def avgfun():
    if not examgrades:#if no average-data returned in the examgrades, the default is zero.
        return 0 #This is where the zero value is returned.
    #If the value for exam grades is added, the sum of data is devided by the length.
    mean = round(sum(examgrades) / len(examgrades), 2) #The 'round' is used to 2 decimal places. The sum of grades divided by the amount of grades calculates the average.
    return mean #This returns the mean count that will reflect for the average function. When the function is called, the mean value is what will appear in the print.

#This is the median function.
def medianfun():
    if not examgrades:#if no median-data is returned for examgrades, the value is returned as zero.
        return 0#Here the value of zero is returned if no ither value is calculated.
    sortedgrades = sorted(examgrades)#The grades are sorted from least to greatest.
    total = len(sortedgrades) #This is where the total amount of numbers listed are counted by the program using 'len'.
    mid = total // 2 #The 'mid' is the middle number. Using'/' will return an float rather than a integer.
    if total % 2 == 0: #If statement is created to take into account the total of the items. This is is in a circumstance that the amount of items are an even amount and there is no middle number.
        mediannumber = (sortedgrades[mid - 1] + sortedgrades[mid]) / 2 #If there is an even amount, 'mid -1' gets the number before the 'middle' and 'mid' is the default sequential number. These are added then divided by 2.
    else: #If not an even amount of numbers, there are an odd amount. In this circumstance, there is one middle number.
        mediannumber = sortedgrades[mid] #The middle number would be pulled here

    return round(mediannumber, 2) #The median number is returned here to 2 decimal places.

#This is the mode function.
def modefun():
    from collections import Counter #Using the collections module, the counter class is used to treat all the split values like 'dict' counts words.
    if not examgrades: #if no mode-data is returned from examgrades, the following is returned.
        return "The data in the file provided has no mode."#The user is let known that there is no mode.
    count = Counter(examgrades) #The 'count' variable is created here. This utilizes the function of the counter class for the examgrades.
    maxcount = max(count.values()) #The max count in the counted values is produced here.
    #The following variable is the counter for the modes. User input brackets allows this to be calculated.
    modes = [num for num, freq in count.items() if freq == maxcount] #num for num, freq in count: counts the items. 
    return modes if len(modes) > 1 else modes[0]#This will ensure only values over 'one' are calculcated. Anything else is a 'zero' if an error exists.

def largestfun(): #This will return the highest value in the listed items for grades.txt.
        with open('grades.txt', 'r') as file: #The 'with open' in the main() is reiterated here - This is here again for debugging reasons.
            examgrades = [int(num) for num in file.readline().strip().split()]
        if not examgrades: #If no max value is returned, the following will happen.
            return "No 'largest' integer is returned." #The user is let known that there is an issue with the output.
        largest = max(examgrades) #The largest integer is found here, the 'max' is pulled from examgrades.
        return largest #The 'largest' value is returned for when the function is called from the menu.

def smallestfun(): #This will return the smallest integer/grade in the listed items for grade.txt.
        with open('grades.txt', 'r') as file: #The 'with open' in the main() is reiterated here - This is here again for debugging reasons.
            examgrades = [int(num) for num in file.readline().strip().split()]
        if not examgrades: #If no min value is returned, the following will happen.
            return "No 'largest' integer is returned." #The user is let known that there is an issue with the output.
        smallest = min(examgrades) #The smallest integer is found here, the 'min' is pulled from examgrades.
        return smallest #The 'smallest' value is returned for when the function is called from the menu.
    
    
if __name__ == "__main__": #DO NOT DELETE
    main()
#END OF PROGRAM


    
