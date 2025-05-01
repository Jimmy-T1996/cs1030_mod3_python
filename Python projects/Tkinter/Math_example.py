from tkinter import *

#Using 'input' opens the terminal

root = Tk()

root.title("Add to 5")

entry_math = Entry(root, width=50, borderwidth=8)
entry_math.pack()
entry_math.insert(0, "Enter a number")

def math_total():
    try:
        user_input = int(entry_math.get())
        total_math = 5 + user_input
        math_label = Label(root, text=f"5 + {user_input} = {total_math}")
        math_label.pack()
    except ValueError:
        error_label = Label(root, text="please enter a number.")
        error_label.pack()

math_button = Button(root, text="Add to 5!!!", padx=50, command=math_total)

math_button.pack()

root.mainloop()
