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
        try:
            with open("data.json", "r") as data:
                # reading old data
                data_read = json.load(data)
                # print(data_read)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                # Saving updated data
                json.dump(new_data, data, indent=4)
        else:
            # Updating old data with new data
            data_read.update(data)
            with open("data.json", "w") as data:
                # Saving updated data
                json.dump(new_data, data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    searchbar = website_entry.get()
    try:
        with open("data.json", "r") as search:
            data_search = json.load(search)
    except FileNotFoundError:
        messagebox.showinfo(title="No Info", message="No Data File Found")
    else:
        if searchbar in data_search:
            email = data_search[searchbar]["email"]
            password = data_search[searchbar]["password"]
            messagebox.showinfo(message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {searchbar} exists")

    searchbar = website_entry.get().title()
    # else:
    #    messagebox.showinfo(title="Try Again", message="No Details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", fg=WHITE, font=(FONT_NAME, 20))
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", fg=WHITE, font=(FONT_NAME, 20))
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", fg=WHITE, font=(FONT_NAME, 20))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()
website_entry.insert(0, string="")

user_entry = Entry(width=39)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.focus()
user_entry.insert(0, string="example@email.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)
password_entry.focus()
password_entry.insert(0, string="")

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, bg=WHITE, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=12, bg=WHITE, command=find_password)
search_button.grid(column=2, row=1)



window.mainloop()