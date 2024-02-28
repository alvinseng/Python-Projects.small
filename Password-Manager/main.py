from tkinter import *
WHITE = "#ffffff"
FONT_NAME = "Courier"
BLACK = "#000000"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#website box labels
website_label = Label(text="Website:", bg=WHITE, fg=BLACK, font=(FONT_NAME, 15))
website_label.grid(column=0, row=1)
website_entry = Entry(width=35, bg=WHITE, fg=BLACK, highlightthickness=0)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1, columnspan=2)

# User Label
user_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK, font=(FONT_NAME, 15))
user_label.grid(column=0, row=2)
user_entry = Entry(width=35, bg= WHITE, fg=BLACK, highlightthickness=0)
user_entry.insert(END, string="")
user_entry.grid(column=1, row=2, columnspan=2)

#Password label
password_label = Label(text="Password:", bg=WHITE, fg=BLACK, font=(FONT_NAME, 15))
password_label.grid(column=0, row=3)
password_entry = Entry(width=21, bg=WHITE, fg=BLACK, highlightthickness=0)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

#Generate password box
generate_password_button = Button(text="Generate Password", bg=WHITE, width=14, borderwidth=0)
generate_password_button.grid(column=2, row=3)

#add password box
add_button = Button(text="Add", width=36, bg=WHITE, borderwidth=0)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()