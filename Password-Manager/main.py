from tkinter import *
from tkinter import messagebox
import random
WHITE = "#ffffff"
FONT_NAME = "Courier"
BLACK = "#000000"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

nr_letters = random.randint(8,10)
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letter_list = ""
for char in range(0, nr_letters):
    letter_list += letters[random.randint(0, len(letters) - 1)]

sym_list = ""
for sym in range(0, nr_symbols):
    sym_list += symbols[random.randint(0, len(symbols) - 1)]

num_list = ""
for num in range(0, nr_numbers):
    num_list += numbers[random.randint(0, len(numbers) - 1)]

combine = letter_list + sym_list + num_list
total = nr_letters + nr_symbols + nr_numbers

generate = random.sample(combine, total)

password_generate = "".join(generate)

print(f'{password_generate}')

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                                                      f"\n Password: {password} \n Is it ok the save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website box labels
website_label = Label(text="Website:", fg=WHITE, font=(FONT_NAME, 15))
website_label.grid(column=0, row=1)
website_entry = Entry(width=39, bg=WHITE, fg=BLACK)
website_entry.focus()
website_entry.insert(0, string="")
website_entry.grid(column=1, row=1, columnspan=2)

# User Label
user_label = Label(text="Email/Username:", fg=WHITE, font=(FONT_NAME, 15))
user_label.grid(column=0, row=2)
user_entry = Entry(width=39, bg=WHITE, fg=BLACK)
user_entry.focus_get()
user_entry.insert(0, string="example@email.com")
user_entry.grid(column=1, row=2, columnspan=2)

# Password label
password_label = Label(text="Password:", fg=WHITE, font=(FONT_NAME, 15))
password_label.grid(column=0, row=3)
password_entry = Entry(width=22, bg=WHITE, fg=BLACK, highlightthickness=0)
password_entry.focus_get()
password_entry.insert(0, string="")
password_entry.grid(column=1, row=3)

# Generate password box
generate_password_button = Button(text="Generate Password", bg=WHITE, borderwidth=0)
generate_password_button.grid(column=2, row=3)

# add password box
add_button = Button(text="Add", width=36, bg=WHITE, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()