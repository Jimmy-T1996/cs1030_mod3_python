from tkinter import *

#required
root = Tk()

def clicktext():
    myLabel = Label(root, text="This is a test")
    myLabel.pack()
    
#calling a function for a button does not need '()' when writing command.
#fg = foreground / bg = background | colors must be quoted. Hex colors work as well.
mybutton = Button(root, text = "Click Me", padx=50, command=clicktext, fg="red", bg="blue")

mybutton.pack()

root.mainloop()
