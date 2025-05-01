from tkinter import *

#required
root = Tk()

# Entry is used to get inputs from the user. this box will get added to root(GUI). the width is 50px wide and has a border of 8 px.
e = Entry(root, width=50, borderwidth=8)
#This method adds the box to the GUI.
e.pack()
'''e.get()'''
#Using the 'e' in column 0 (the only box), a default text is added to tell the user to get their name.
e.insert(0, "enter your name: ")


#This function is the output after entering your name.
def clicktext():
    #This variable creates the greeting for the user, e.get() returns the input from the 'e' variable.
    hello = "hello " + e.get()
    #Labels are used to display information. 'Label' gets added to root (GUI) and uses the text from 'hello' variable.
    myLabel = Label(root, text=hello)
    #This inserts the label to root.
    myLabel.pack()

#The following button has a syntax line of command=clicktext which calls the function.    
#calling a function for a button does not need '()' when writing command.
#fg = foreground / bg = background | colors must be quoted. Hex colors work as well.
mybutton = Button(root, text = "Enter your name", padx=50, command=clicktext, fg="red", bg="blue")

#button is added to root
mybutton.pack()


#Keeps program running.
root.mainloop()
