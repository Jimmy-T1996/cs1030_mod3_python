'''
Author: Jimmy Torres
Program: Password Generator
Last Date Edited:
Date Created:

Notes: 
Working------------
Main window working
-dark theme applied to everything
-font and buttons created

NOT working
-All buttons are not configured
-Too much code
-encryption not implemented
-styling needs work

'''


from tkinter import * #tkinter needed for GUI construction
from PasswordGenerator import char_list1,char_list2 #Character lists in original PasswordGenerator file.
from PIL import Image, ImageTk #Pillow library added to add and modify logo in the GUI main menu.
import random #Random used for randomly generated functions.
import csv
import os
from cryptography.fernet import Fernet
root = Tk() #root is essentially the GUI windows. (does not run in python terminal)
root.title("Password Generator") #Title of GUI

root.configure(bg="#2e2e2e") #Background color of dark grey added to all windows
btn_bg = "#444" #Lighter grey buttons gives contrast.
btn_fg = "white" #White text to make it readable.
btn_active_bg = "#555" #When button is clicked on, different grey is shown. If deleted, button turns white.
default_font = ("Courier New", 12, "bold") # Font, text size, bold text

#This list will be used to store the individually generated characters of each password.
#This also gets cleared with every password iteration.
randlist = []
#Joined characters will create an output(password) and be saved here. 
new_password = []
#This list serves as the content needed to write and save new .txt files.
password_output = []

title = []
username = []
password = []

#When this function is called, a new window is opened with a different GUI.
def password_gen1():

    
    # New window is created and becomes the "top level". If this window is closed, program is still running.
    new_window = Toplevel(root)
    new_window.title("Password Generator")
    new_window.geometry("700x950")
    new_window.configure(bg="#2e2e2e")
    
    btn_bg = "#444"
    btn_fg = "white"
    default_font = ("Courier New", 12, "bold")

    # Give column 0 room to expand
    new_window.columnconfigure(0, weight=1)

    # Widgets
    instruction_char = Label(new_window, text="How many Characters Do \nYou need In Your Password?", bg=btn_bg, fg=btn_fg, font=default_font)
    user_input1 = Entry(new_window, width=35, border=8)

    instruction_passwords = Label(new_window, text="How Many Passwords Do \nYou Need?", bg=btn_bg, fg=btn_fg, font=default_font)
    user_input2 = Entry(new_window, width=35, border=8)

    generate_password = Button(new_window, text="Generate with special characters", bg=btn_bg, fg=btn_fg, font=default_font,
                                command=lambda: generate_1(user_input1.get(), user_input2.get()))
    generate_password2 = Button(new_window, text="Generate WITHOUT special characters", bg=btn_bg, fg=btn_fg, font=default_font,
                                 command=lambda: generate_2(user_input1.get(), user_input2.get()))
    close_btn = Button(new_window, text="Close", command=new_window.destroy, bg=btn_bg, fg=btn_fg, font=default_font)

    global output
    output = Text(new_window, width=60, height=25, bg="gray", fg="black", font=("Courier New", 12, "bold"))
    output.tag_configure("center", justify='center')
    output.insert("1.0", "Passwords Generated here")
    output.tag_add("center", "1.0", "end")
    output.configure(state="disabled")

    # Layout
    instruction_char.grid(row=0, column=0, pady=10)
    user_input1.grid(row=1, column=0, pady=20, padx=10)

    instruction_passwords.grid(row=2, column=0, pady=10)
    user_input2.grid(row=3, column=0, pady=20, padx=10)

    generate_password.grid(row=4, column=0, pady=15)
    generate_password2.grid(row=5, column=0, pady=15)
    close_btn.grid(row=6, column=0, pady=15)

    output.grid(row=7, column=0, pady=20)




def sos():
    new_window = Toplevel(root)  
    new_window.title("Passwords Information")
    new_window.geometry("800x400")
    new_window.configure(bg="#2e2e2e")
    btn_bg = "#444"
    btn_fg = "white"
    btn_active_bg = "#555"
    default_font = ("Courier New", 12, "bold")

    new_window.columnconfigure(0, weight=1)
    new_window.columnconfigure(1, weight=0)
    new_window.columnconfigure(2, weight=1)

    password_info = Label(new_window,
                          text="    Password creation does not need to be complicated, but it " \
                          "does need to be well thought out. The Cybersecurity & Infrastructure" \
                          " Security Agency (CISA) recommends that a user has a password length " \
                          "of ATLEAST 16 characters.\n    This should include numbers, special characters, " \
                          "non-related phrases — if you plan to include phrases at all. When creating a " \
                          "long list of accounts with various passwords, you should be able to access " \
                          "them. CISA also reccomends you use a reputable password manager. Ensure that " \
                          "you do not re-use passwords for several accounts and that your passwords do not " \
                          "follow a naming convention, such as: 'Password2023' and '20Password23'.\n"
                          "    If Multifactor Authentication is offered by the services you are using, " \
                          "it is recommended to set up the service to mitigate any possible exploits." \
                          "CISA currently reports that 99% of user who implement MFA, do not get hacked.\n"
                          "    For more information on password creation, please visit:\n"
                          "https://www.cisa.gov/secure-our-world/use-strong-passwords",
                            bg=btn_bg, fg=btn_fg, font=default_font, wraplength=700, justify="left")
    password_info.grid(row=0, column=1)

    close_btn = Button(new_window, text="Close", command=new_window.destroy, bg=btn_bg, fg=btn_fg, font=default_font)
    close_btn.grid(row=1, column=1, pady=10)

def password_manager():
    new_window = Toplevel(root)  
    new_window.title("Password Manager")
    new_window.configure(bg="#2e2e2e")
    btn_bg = "#444"
    btn_fg = "white"
    btn_active_bg = "#555"
    default_font = ("Courier New", 12, "bold")

    button_first = Button(new_window, text="Edit Account List", height=4, width=60,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg, 
                      font=default_font, command=create_account) 
    button_second = Button(new_window, text="View Account List", height=4, width=60,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg, 
                      font=default_font, command=view_accounts) 
    close_btn = Button(new_window, text="Close", command=lambda: encrypt_and_close(new_window), bg=btn_bg, fg=btn_fg, font=default_font)


#The Placement of the Image and buttons on the first menu are formatted here.
#Second button removed. The second button function was moved into button_first for simplicity.
    button_first.grid(row=1, column=0, columnspan=4, padx=12, pady=10)
    button_second.grid(row=2, column=0, columnspan=4, padx=12, pady=10)
    close_btn.grid(row=3, column=0, columnspan=4, padx=12, pady=10)

def create_account():
    new_window = Toplevel(root)  
    new_window.title("Account List Creator")
    new_window.configure(bg="#2e2e2e")
    btn_bg = "#444"
    btn_fg = "white"
    default_font = ("Courier New", 12, "bold")

    title_instruction = Label(new_window, text="Enter Title of Account", bg=btn_bg, fg=btn_fg, font=default_font)
    title_input = Entry(new_window, width=35, border=8)

    username_instruction = Label(new_window, text="Enter Username", bg=btn_bg, fg=btn_fg, font=default_font)
    username_input = Entry(new_window, width=35, border=8)

    password_instruction = Label(new_window, text="Enter Password", bg=btn_bg, fg=btn_fg, font=default_font)
    password_input = Entry(new_window, width=35, border=8)
    
    button_first = Button(new_window, text="add account", width=35, bg=btn_bg, fg=btn_fg, font=default_font, command=lambda: input_function(title_input.get(), username_input.get(), password_input.get())) 
    
    delete_instruction = Label(new_window, text="Enter the Title of the Account\nyou want to delete:", bg=btn_bg, fg=btn_fg, font=default_font)
    delete_input = Entry(new_window, width=35, border=8)
    delete_btn = Button(new_window, text="Delete Account", command=lambda: delete_account(delete_input, delete_confirm), bg=btn_bg, fg=btn_fg, font=default_font)
    delete_confirm = Text(new_window, width=35, height=1, bg="gray", fg="black", font=("Courier New", 12, "bold"))

    close_btn = Button(new_window, text="Close", command=new_window.destroy, bg=btn_bg, fg=btn_fg, font=default_font)


#The Placement of the Image and buttons on the first menu are formatted here.
#Second button removed. The second button function was moved into button_first for simplicity.
    title_instruction.grid(row=0, column=0, columnspan=4)
    title_input.grid(row=1, column=0, columnspan=4, pady=20, padx=20)

    username_instruction.grid(row=2, column=0, columnspan=4)
    username_input.grid(row=3, column=0, columnspan=4, pady=20, padx=20)

    password_instruction.grid(row=4, column=0, columnspan=4)
    password_input.grid(row=5, column=0, columnspan=4, pady=20, padx=20)

    button_first.grid(row=6, column=0, columnspan=4, padx=20, pady=10)

    delete_instruction.grid(row=7, column=0, columnspan=4, pady=25)
    delete_input.grid(row=8, column=0, columnspan=4, pady=15, padx=20)
    delete_btn.grid(row=9, column=0, columnspan=4, padx=20, pady=10)
    delete_confirm.grid(row=10, column=0, columnspan=4, padx=20, pady=10)

    close_btn.grid(row=11, column=0, columnspan=4, padx=25, pady=10)

    return title_input, username_input, password_input, delete_input

def view_accounts():
    decrypt_file()
    new_window = Toplevel(root)  
    new_window.title("Account List")
    new_window.configure(bg="#2e2e2e")

    # Create the Text widget first
    accounts_box = Text(new_window, width=60, height=25, bg="gray", fg="black", font=("Courier New", 12, "bold"))
    accounts_box.grid(row=0, column=0, pady=20)

    # Then load the CSV into it
    titles, usernames, passwords, accounts = read_columns("Password.csv")

    # Insert the accounts into the Text box
    for t, u, p in zip(titles, usernames, passwords):
        accounts_box.insert("end", f"Title: {t} \nUsername: {u} \nPassword: {p}\n\n")

    # (Optional) Make it read-only after inserting
    accounts_box.configure(state="disabled")

def generate_1(user_input1, user_input2):
    output.configure(state="normal")
    output.delete("1.0", END)  

    if not user_input1.isdigit() or not user_input2.isdigit():
        output.insert("1.0", "A number must be entered", "center")  # Use "1.0" instead of 0
    else:
        char_count = int(user_input1)
        password_count = int(user_input2)
        generate_1_2(char_count, password_count)

    output.configure(state="disabled")  # Use "disabled" not "readonly"

def generate_2(user_input1, user_input2):
    output.configure(state="normal")
    output.delete("1.0", END)  # Correct way to clear Text widget

    if not user_input1.isdigit() or not user_input2.isdigit():
        output.insert("1.0", "A number must be entered", "center")  # Use "1.0" instead of 0
    else:
        char_count = int(user_input1)
        password_count = int(user_input2)
        generate_2_2(char_count, password_count)

    output.configure(state="disabled")  # Use "disabled" not "readonly"
      

def generate_1_2(char_count, password_count):
    for outputs in range (password_count):
        #Because this is a for loop, randlist will need to be cleared everytime it starts.
        #This is required for making several passwords individually or they will stack on eachother.
        randlist.clear()
        #This for loop is for the individual password length. Char_count was the user input.
        for items in range (char_count):
            #with 80 list items in char_list, randselection finds a random number in this range.
            randselection = random.randint(0,79)
            #The previous random number is matched to the char_list1 list and a character is selected.
            get_rand_char = (char_list1[randselection])
            #The randlist will collect all the random chracters in char_list1 and save them here as a new list.
            randlist.append(get_rand_char)
        #This variable joins the seperated string character and forms the password.
        new_password ="".join(randlist)
        #The new password is appended/added to password output(outside of randlist). This is for saving txt files.
        password_output.append(new_password)
        output.configure(state="normal")
        output.insert("end", f"NEW PASSWORD: {new_password}\n", "center")
        output.configure(state="disabled")
def generate_2_2(char_count, password_count):
    for outputs in range (password_count):
        #Because this is a for loop, randlist will need to be cleared everytime it starts.
        #This is required for making several passwords individually or they will stack on eachother.
        randlist.clear()
        #This for loop is for the individual password length. Char_count was the user input.
        for items in range (char_count):
            #with 80 list items in char_list, randselection finds a random number in this range.
            randselection = random.randint(0,59)
            #The previous random number is matched to the char_list1 list and a character is selected.
            get_rand_char = (char_list2[randselection])
            #The randlist will collect all the random chracters in char_list1 and save them here as a new list.
            randlist.append(get_rand_char)
        #This variable joins the seperated string character and forms the password.
        new_password ="".join(randlist)
        #The new password is appended/added to password output(outside of randlist). This is for saving txt files.
        password_output.append(new_password)
        output.configure(state="normal")
        output.insert("end", f"NEW PASSWORD: {new_password}\n", "center")
        output.configure(state="disabled")

def input_function( title_input, username_input, password_input):
    if title_input.strip() == ['', '  ', '   ']:
        print("A title is required.")
        #The username and password are only requested as input if a title is created.
        #All (3) inputs are appended to their appropriate list.
    else:
        title.append(title_input)
        username.append(username_input)
        password.append(password_input)

        file_exists = os.path.isfile("Password.csv")  # Check if file already exists
        
        with open("Password.csv", "a", newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                # If the file doesn't exist, write headers first
                writer.writerow(["Title", "Username", "Password"])
            
            for i in range(len(title)):
                writer.writerow([title[i], username[i], password[i]])
def read_columns(filename):
    titles = []
    usernames = []
    passwords = []
    accounts = []

    with open(filename, "r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            titles.append(row["Title"])
            usernames.append(row["Username"])
            passwords.append(row["Password"])
            accounts.append(row)

    return titles, usernames, passwords, accounts

def read_accounts(filename):
    accounts = []
    with open("Password.csv", "r", newline='') as file:
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
        return False  # No account found

    # Write the updated list back to the file
    with open(filename, "w", newline='') as file:
        fieldnames = ["Title", "Username", "Password"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_accounts)
    
    return True  # Account deleted successfully

def delete_account(delete_input, delete_confirm):
    title_to_delete = delete_input.get().strip()
    deleted = delete_account_by_title("Password.csv", title_to_delete)

    delete_confirm.configure(state="normal")
    delete_confirm.delete("1.0", "end")
    if deleted:
        delete_confirm.insert("end", f"Deleted account: {title_to_delete}")
        delete_input.delete(0, "end")  # Clear input
        delete_confirm.configure(fg="red")  # Success color
    else:
        delete_confirm.insert("end", f"No account found with title: {title_to_delete}")
        delete_confirm.configure(fg="red")  # Error color
    delete_confirm.configure(state="disabled")

def key_loader():
    with open('mykey.key', 'rb') as key_file:
        return key_file.read()

def decrypt_file():
    key = key_loader()
    f = Fernet(key)

    with open('Password.csv', 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open('Password.csv', 'wb') as file:
        file.write(decrypted_data)

def encrypt_file():
    key = key_loader()
    f = Fernet(key)

    with open('Password.csv', 'rb') as file:
        decrypted_data = file.read()

    encrypted_data = f.encrypt(decrypted_data)

    with open('Password.csv', 'wb') as file:
        file.write(encrypted_data)

def encrypt_and_close(window):
    encrypt_file()   # <-- Encrypt the file first
    window.destroy() # <-- Then close the window


#--------This section is only aesthetic. ChatGPT was used as last resort to troubleshoot loading png file with 
# transparent values image into GUI.------------

#Logo for GUI loaded here. Pillow is used for manipulating the image properties. Image is entirely resampled.

#Image is opened. Convert method switches to RGBA values because the image is a PNG file with transparent values.
devildog = Image.open("devildog.png").convert("RGBA")
#Image is resized to avoid incorrect aspect ratio. Lanczos algorithm is the logic behind the resampling.
devildog = devildog.resize((150, 135), Image.Resampling.LANCZOS)

#Skullimage formats the devildog image to be used with Tkinter.
skull_image = ImageTk.PhotoImage(devildog)
#The Label datatype is added to the skull_image variable and formatted in this variable.
#*** bg=root["bg"] is an undefined variable that allows the image to have a background with no value.
skull_image_label = Label(root, image=skull_image, bg=root["bg"], width=150, height=150)
#Image is displayed.
skull_image_label.image = skull_image 
#--------End of AI section. -----------------

#Thes variables are for the buttons in the first menu in the GUI.
#Sizing, properties, and logic of these buttons are here.
button_first = Button(root, text="Password Generator", height=4, width=60,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg, 
                      font=default_font, command=password_gen1) 
button_third = Button(root, text="More Info On Passwords ", height=4, width=60,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg, 
                      font=default_font, command=sos) 
button_fourth = Button(root, text="Password Manager", height=4, width=60,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg, 
                      font=default_font, command=password_manager) 


#The Placement of the Image and buttons on the first menu are formatted here.
#Second button removed. The second button function was moved into button_first for simplicity.
skull_image_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
button_first.grid(row=1, column=0, columnspan=4, padx=10, pady=(15, 1))
button_third.grid(row=2, column=0, columnspan=4, padx=10, pady=1)
button_fourth.grid(row=3, column=0, columnspan=4, padx=10, pady=(1, 15))


#*** DO NOT CHANGE *** This function is what keeps the GUI window continuously working.
root.mainloop()