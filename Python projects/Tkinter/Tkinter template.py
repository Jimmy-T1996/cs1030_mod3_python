from tkinter import *

root = Tk()
root.title("Template")

root.configure(bg="#2e2e2e")
btn_bg = "#444"
btn_fg = "white"
btn_active_bg = "#555"

def password_gen1():
    pass



button_first = Button(root, text="Special Characters | Password Generator", height=4, width=40,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg,
                      command=password_gen1) 
button_second = Button(root, text="No Special Characters | Password Generator", height=4, width=40,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg,
                      command=password_gen1) 
button_third = Button(root, text="More Info On Passwords ", height=4, width=40,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg,
                      command=password_gen1) 
button_fourth = Button(root, text="Password Compare Tool", height=4, width=40,
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_fg,
                      command=password_gen1) 



button_first.grid(row=1, column=0, columnspan=4, padx=10, pady=(15, 1))
button_second.grid(row=2, column=0, columnspan=4, padx=10, pady=1)
button_third.grid(row=3, column=0, columnspan=4, padx=10, pady=1)
button_fourth.grid(row=4, column=0, columnspan=4, padx=10, pady=(1, 15))


root.mainloop()
            
