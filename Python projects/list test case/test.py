
#These lists are for a user to creat a title of what account they are saving, usernames and password.
#These will be written to a file later.
title = []
username = []
password = []


#This function will receive inputs from the user for:
#Title of entry, Username, password. Title input of "done" stops loop.
def input_function():
    while True:
        userinput1 = input("Please enter a Title for the account you are saving, or type 'done' when you are finished:\n")
        if userinput1.lower() == "done":
            break
        elif userinput1 == "":
            print("Title is required.")
        #The username and password are only requested as input if a title is created.
        #All (3) inputs are appended to their appropriate list.
        else:
            userinput2 = input("Please enter a Username:\n")
            userinput3 = input("Please enter a Password:\n")
            title.append(userinput1)
            username.append(userinput2)
            password.append(userinput3)

#Input function is called.
input_function()

#This creates a text file saving all the appended information to a txt file.
while True:
    #If user selects 'y' to save file, the writing process starts.
    user_save = input("save? (y/n): ").lower()
    if user_save == "y":
        #A .txt file named "password" will be written. 
        with open("Password.txt", "w") as file:
            #This is the first line of text that appears at the top of the file.
            file.write("Accounts:\n\n")
            #for loop is started to create a vertical column of information.
            #'i' will be used as the slot of each item being written.
            #The for loop is based on the range/length of items in the 'title' list.
            #Because username and passwords cannot be created with out a title, there should always be information.
            for i in range(len(title)):
                #using [i] as the point of reference, all (3) lists are pulling items from the same placeholders they correlate to in their lists.
                #If there is any reason there is no input in list slot, '---' is printed.
                t = title[i] if i < len(title) else "---"
                u = username[i] if i < len(username) else "---"
                p = password[i] if i < len(password) else "---"
                #The previous syntax only changed the strings assigned to the variables.
                #The next (3) lines print the current items the previous variables pulled from their lists.
                file.write(f"Title: {t}\n")
                file.write(f"Username: {u}\n")
                file.write(f"Password: {p}\n\n")
                #When the loop repeats, the variables will change to the next item in their respective lists.
                #When the lists run out, the loop will stop (max number in range is met).
        #This input is to notify the user of what just happened. They need to read this line to contine.
        input("File was saved and written to your machine. Press any key to continue.")
        break
    #If the user chooses not to save a file, the loop is terminated, nothing is saved.
    elif user_save == "n":
        input("Press any key to return to the menu. \nOtherwise, close this window to exit program.")
        break
    #Bad entries are caught here. loop is repeated.
    else:
        print("Whoops! Please enter 'y' or 'n'.")


