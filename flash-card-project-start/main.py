BACKGROUND_COLOR = "#B1DDC6"
FONT_COLOR = "#000000"
FONT_NAME = "Ariel"

# ----- Words function ------



# ------ UI Setup -------
from tkinter import *

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
flashcard_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=flashcard_img)
canvas.create_text(400, 150, text="French", fill='black', font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 263, text='Words here', fill='black', font=(FONT_NAME, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img)
wrong_button.config(highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column=0, row=1)


correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img)
correct_button.config(highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)






window.mainloop()
