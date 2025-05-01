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
-image label missing above buttons
-password generator not translated into tkinter syntax

'''


from tkinter import *
from PasswordGenerator import char_list1, char_list2
from PIL import Image, ImageTk
import random
root = Tk()
root.title("Password Generator")

root.configure(bg="#2e2e2e")
btn_bg = "#444"
btn_fg = "white"
btn_active_bg = "#555"
default_font = ("Courier New", 12, "bold")

#This list will be used to store the individually generated characters of each password.
#This also gets cleared with every password iteration.
randlist = []
#Joined characters will create an output(password) and be saved here. 
new_password = []
#This list serves as the content needed to write and save new .txt files.
password_output = []

def password_gen1():
    new_window = Toplevel(root)  
    new_window.title("Password Generator")
    new_window.geometry("1500x850")
    new_window.configure(bg="#2e2e2e")
    btn_bg = "#444"
    btn_fg = "white"
    btn_active_bg = "#555"
    default_font = ("Courier New", 12, "bold")

    new_window.columnconfigure(0, weight=1)
    new_window.columnconfigure(1, weight=1)
    new_window.columnconfigure(2, weight=1)

    user_input1 = Entry(new_window, width=35, border=8)
    user_input1.grid(row=0, column=2, columnspan=2, pady=20, padx=20, sticky="w")

    instruction = Label(new_window, text="How many Characters Do \nYou need In Your Password?", bg=btn_bg, fg=btn_fg, font=default_font)
    instruction.grid(row=0, column=0, sticky="e")

    user_input2 = Entry(new_window, width=35, border=8)
    user_input2.grid(row=1, column=2, columnspan=2, pady=20, padx=20, sticky="w")

    instruction = Label(new_window, text="How Many Passwords Do \nYou Need?", bg=btn_bg, fg=btn_fg, font=default_font)
    instruction.grid(row=1, column=0, sticky="e")

    generate_password = Button(new_window, text="Generate with special characters", bg=btn_bg, fg=btn_fg, font=default_font, command=lambda: generate_1(user_input1.get(), user_input2.get()))
    generate_password.grid(row=3, column=1, pady=15)

    generate_password2 = Button(new_window, text="Generate WITHOUT special characters", bg=btn_bg, fg=btn_fg, font=default_font, command=lambda: generate_2(user_input1.get(), user_input2.get()))
    generate_password2.grid(row=4, column=1, pady=15)

    close_btn = Button(new_window, text="Close", command=new_window.destroy, bg=btn_bg, fg=btn_fg, font=default_font)
    close_btn.grid(row=7, column=1, pady=15)

    global output
    output = Text(new_window, width=60, height=25, bg="gray", fg="black", font=("Courier New", 12, "bold")) 
    output.grid(row=5, column=0, columnspan=3, pady=20)
    # Create a centered text tag
    output.tag_configure("center", justify='center')

    # Insert text using the tag
    output.insert("1.0", "Passwords Generated here", "center")
    output.configure(state="disabled")

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
    new_window.columnconfigure(1, weight=1)
    new_window.columnconfigure(2, weight=1)

    user_input = Entry(new_window, width=35, border=8)
    user_input.grid(row=0, column=1, pady=20)

    close_btn = Button(new_window, text="Close", command=new_window.destroy, bg=btn_bg, fg=btn_fg, font=default_font)
    close_btn.grid(row=1, column=1, pady=10)

def password_compare():
    new_window = Toplevel(root)  
    new_window.title("Password Compare Tool")
    new_window.geometry("800x400")
    new_window.configure(bg="#2e2e2e")
    btn_bg = "#444"
    btn_fg = "white"
    btn_active_bg = "#555"
    default_font = ("Courier New", 12, "bold")

    new_window.columnconfigure(0, weight=1)
    new_window.columnconfigure(1, weight=1)
    new_window.columnconfigure(2, weight=1)

    user_input = Entry(new_window, width=35, border=8)
    user_input.grid(row=0, column=1, pady=20)

    close_btn = Button(new_window, text="Close", command=new_window.destroy, bg=btn_bg, fg=btn_fg, font=default_font)
    close_btn.grid(row=1, column=1, pady=10)

def generate_1(user_input1, user_input2):
    output.configure(state="normal")
    output.delete("1.0", END)  # Correct way to clear Text widget

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

devildog = Image.open("devildog.png").convert("RGBA")
devildog = devildog.resize((150, 135), Image.Resampling.LANCZOS)


skull_image = ImageTk.PhotoImage(devildog)

skull_image_label = Label(root, image=skull_image, bg=root["bg"], width=150, height=150)

skull_image_label.image = skull_image 


button_first = Button(root, text="Password Generator", height=4, width=60,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg, 
                      font=default_font, command=password_gen1) 
button_third = Button(root, text="More Info On Passwords ", height=4, width=60,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg, 
                      font=default_font, command=sos) 
button_fourth = Button(root, text="Password Compare Tool", height=4, width=60,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg, 
                      font=default_font, command=password_compare) 


skull_image_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
button_first.grid(row=1, column=0, columnspan=4, padx=10, pady=(15, 1))
button_third.grid(row=2, column=0, columnspan=4, padx=10, pady=1)
button_fourth.grid(row=3, column=0, columnspan=4, padx=10, pady=(1, 15))



root.mainloop()