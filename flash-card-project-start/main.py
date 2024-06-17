BACKGROUND_COLOR = "#B1DDC6"
FONT_COLOR = "#000000"
FONT_NAME = "Ariel"

# ----- Words function ------
import pandas
import random

try:
    data = pandas.read_csv("data/Words_to_learn.csv")
        # print(to_learn)
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=flashcard_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv", index=False)
    next_card()

# ------ UI Setup -------
from tkinter import *

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
flashcard_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=flashcard_img)
card_title = canvas.create_text(400, 150, text="Title", fill='black', font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text='Words', fill='black', font=(FONT_NAME, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,  highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)


correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
correct_button.grid(column=1, row=1)

next_card()


window.mainloop()
