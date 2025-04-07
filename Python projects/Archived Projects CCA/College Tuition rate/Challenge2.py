"""
Program: Challenge2.py
Author: Jaime Torres
Last Date Modified: 7/21/2024

Purpose: This program will calculate a tuition increase as an input by
the user for tuition rates over a span of 5 years at Community College of Aurora.
The table in the output will also include the first year as a baseline with the
subsequent 5 years in the table.
"""


#Function to calculate tuition for each year based on initial tuition and rate increase
def calculate_tuition(initial_tuition, tuition_rate, years):
    tuitions = []#Calculated tuition with user input will be saved here for return.
    current_tuition = initial_tuition
    for year in range(years):
        tuitions.append(current_tuition)#This allows the data to be appended to the end of the
                                        #list as it is calculated based on the range of years provided.

        current_tuition += current_tuition * tuition_rate #current tuition is multiplied by tuition rate.
    return tuitions #tuition is returned from line 14.

# Function to calculate compound interest for each year
def calculate_cca_interest(principal, annual_rate, years, periods_per_year=1):
    interest_data = []
    for year in range(years):
        amount = principal * (1 + annual_rate / periods_per_year) ** (periods_per_year * year)
        interest_data.append(amount)
    return interest_data #the interest data has now updated and the new value is returned here

#User inputs are shown in program here.
#Below is the request for the tuition rate as a whole number and then converted to a percent total.
input_tuitrate = int(input("Please enter a Tuition rate % as a whole number: "))
tuitrate = input_tuitrate / 100
#The user will then enter the total number of years to attend school.
input_tuityears = int(input("Please enter total amount of years to attend school: "))
#The total amount of credit hours per year will be entered.
input_credithours = int(input("Please enter total amount of credit hours per year as a whole number: "))

#Using the CCA_Costs.txt file in the same directory as this program, the tuition rate will be calculated.
with open('CCA_Costs.txt', 'r') as file:
    data = file.readlines()

#The file data is stripped and converted into a float value for a money calculation.
tuition_data = [float(line.strip()) for line in data]

#The first calculation is done at year zero(first year) and will calculate based on the base cost.
tuitions = calculate_tuition(tuition_data[0], tuitrate, input_tuityears)


initial_principal = tuitions[0] * input_credithours#Starting with principal/initial amount owed, this total is calculated. 
annual_rate = tuitrate #this is here to rename and keep track of what this value is.
interest_data = calculate_cca_interest(initial_principal, annual_rate, input_tuityears)#The interest data function is called with all inputs.

#The header is created here. Everything past this line calculates the Output table.
print("%4s%28s" % ("Year", "Total Cost"))

with open('TuitionResults.txt', 'w') as output_file: #this outputs a new file called, Tuitionresults.txt using 'write'
    
    #For each year in the range of years provided by the user, the listed table is printed here.
    for year in range(input_tuityears):
        output_file.write("%4s%28s\n" % ("Year", "Total Cost")) #This will create the header inside the new file.

        #The tuition * the amount of credit hours is calculated here.
        year_tuition = tuitions[year]#The tuition will be formatted with corresponding year
                                     #in the square brackets from the listed range of years.
                                     #This value is what will be shown in the financial total
                                     #of the output table.
        year_total_tuition_cost = year_tuition * input_credithours#The year tuition has not taken account of
                                                           #credit hours and is calculated here.

        year_interest = interest_data[year] #The year interest is calculated based on how many years was input.
        year_total_cost = year_total_tuition_cost + year_interest #the year interest(isolated) is added to the year tuition, result is the year total.

        output_file.write(f"{year + 1:4}                   ${year_total_cost:.2f}\n") #this writes the data to the output .txt file.
        
        # Display year, total tuition cost, and total cost with compound interest formatted
        print(f"{year + 1:4}                   ${year_total_cost:.2f}\n")

print("Data output written to TuitionResults.txt")#This is displayed to user in the program.
# Close the file
file.close()
# END OF PROGRAM

