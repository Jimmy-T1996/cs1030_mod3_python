import csv
import os

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

#This writes and appends to existing list
while True:
    user_save = input("save? (y/n): ").lower()
    if user_save == "y":
        file_exists = os.path.isfile("Password.csv")  # Check if file already exists
        
        with open("Password.csv", "a", newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                # If the file doesn't exist, write headers first
                writer.writerow(["Title", "Username", "Password"])
            
            for i in range(len(title)):
                writer.writerow([title[i], username[i], password[i]])
        
        input("File was saved and written to your machine. Press any key to continue.")
        break
    elif user_save == "n":
        input("Press any key to return to the menu. \nOtherwise, close this window to exit program.")
        break
    else:
        print("Whoops! Please enter 'y' or 'n'.")

#This reads file and displays information-------------------------------------------
def read_columns(filename):
    titles = []
    usernames = []
    passwords = []

    with open(filename, "r", newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            titles.append(row["Title"])
            usernames.append(row["Username"])
            passwords.append(row["Password"])

    return titles, usernames, passwords

# Example usage:
titles, usernames, passwords = read_columns("Password.csv")

# Print by row
for t, u, p in zip(titles, usernames, passwords):
    print(f"Title: {t} | Username: {u} | Password: {p}")

def read_accounts(filename):
    accounts = []
    with open(filename, "r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            accounts.append(row)
    return accounts

def delete_account_by_title(filename, title_to_delete):
    accounts = read_accounts(filename)
    
    # Filter out the accounts where title matches
    updated_accounts = [account for account in accounts if account["Title"] != title_to_delete]

    # Check if any account was deleted
    if len(accounts) == len(updated_accounts):
        print("No account found with that title.")
        return

    # Write the updated list back to the file
    with open(filename, "w", newline='') as file:
        fieldnames = ["Title", "Username", "Password"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_accounts)
    
    print(f"Account with title '{title_to_delete}' was deleted successfully.")

# Example usage:
title_input = input("Enter the title of the account you want to delete: ")
delete_account_by_title("Password.csv", title_input)





