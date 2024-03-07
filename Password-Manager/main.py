import random
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

WHITE = "#ffffff"
FONT_NAME = "Courier"
BLACK = "#000000"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8,10))]
    # for char in range(0, nr_letters):
    #     letter_list += letters[random.randint(0, len(letters) - 1)]

    sym_list = [choice(symbols) for _ in range(randint(2,4))]
    # for sym in range(0, nr_symbols):
    #     sym_list += symbols[random.randint(0, len(symbols) - 1)]

    num_list = [choice(numbers) for num in range(randint(2,4))]
    # for num in range(0, nr_numbers):
    #     num_list += numbers[random.randint(0, len(numbers) - 1)]

    combine = letter_list + sym_list + num_list
    shuffle(combine)

    password_generate = "".join(combine)
    password_entry.insert(0, password_generate)
    pyperclip.copy(password_generate)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        with open("data.json", "r") as data:
            # reading old data
            data_read = json.load(data)
            # print(data_read)
            # Updating old data with new data
            data_read.update(data)

        with open("data.json", "r") as data:
            # Saving updated data
            json.dump(new_data, data, indent=4)

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
generate_password_button = Button(text="Generate Password", bg=WHITE, borderwidth=0, command=password_generator)
generate_password_button.grid(column=2, row=3)

# add password box
add_button = Button(text="Add", width=36, bg=WHITE, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()