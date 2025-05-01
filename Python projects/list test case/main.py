


title = []
username = []
password = []
storage = [[title],[username], [password]]

#This function saves inputs to the userinputs list.
def input_function():
    #While true starts a loop while boolean is implemented.
    while True:
        #This takes inputs by the user.
        userinput1 = input("Please enter an input to save, type 'done' when you are finished:\n")
        #This stops the loop.
        if userinput1 == "done":
            break
        elif userinput1 == "":
            print("Title is required.")
        #This adds all userinput values that are not 'done' to the userinputs list.
        else:
            userinput2 = input("Please enter a Username:\n")
            userinput3 = input("Please enter a Password:\n")
        title.append(userinput1)
        username.append(userinput2)
        password.append(userinput3)
#This starts the function when program is started.    
input_function()


""" while any(storage):
    log=[]
    for account in storage:
        if account:
            log.append(account.pop(0))
        else:
            log.append("---")

    for line in log:
        print (f"{line}")
    print(" ") """

""" while True:
        user_save = input("save? :   ").lower()
        if user_save == "y":
            with open(f"Password.txt", "w") as file:
                file.write("Accounts:\n")
                for account in storage:
                    if account:
                        file.write(title.pop(0),"\n")
                        file.write(username.pop(0),"\n")
                        file.write(password.pop(0),"\n")
                    else:
                        file.write("---")
                

                file.close()
                input("Press any key to return to menu or close this window.")
        elif user_save == "n":
            input("Press any key to return to the menu. \nOtherwise, close this window to exit program.")
        else:
            print("Whoops! Please enter 'y' or 'n'.") """

while True:
    user_save = input("save? (y/n): ").lower()
    
    if user_save == "y":
        with open("Password.txt", "w") as file:
            file.write("Accounts:\n")
            
            while any(storage):
                t = title.pop(0) if title else "---"
                u = username.pop(0) if username else "---"
                p = password.pop(0) if password else "---"
                
                file.write(f"{t}\n")
                file.write(f"{u}\n")
                file.write(f"{p}\n")
                file.write("\n")  # Blank line between entries

        input("Saved! Press any key to return to menu or close this window.")
        break  # Exit the loop after saving

    elif user_save == "n":
        input("Press any key to return to the menu. \nOtherwise, close this window to exit program.")
        break  # Exit the loop if user says no

    else:
        print("Whoops! Please enter 'y' or 'n'.")
          