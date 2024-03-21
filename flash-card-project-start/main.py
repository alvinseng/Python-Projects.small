BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
CARD_FRONT = "images/card_front.png"
CARD_BACK = "../images/card_back.png"
WRONG_BUTTON = "../images/wrong.png"
CORRECT_BUTTON = "../images/right.png"

# ----- Words function ------



# ------ UI Setup -------
from tkinter import *
import random

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
flashcard_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=flashcard_img, bg=BACKGROUND_COLOR)
flashcard_top_txt = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

flashcard_french_words = canvas.create_text(400, 263, text='Enter french words here', font=(FONT_NAME, 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0)
correct_button.grid(column=1, row=1)






window.mainloop()
