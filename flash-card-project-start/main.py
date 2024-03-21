
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# --- UI Setup ----
from tkinter import *

window = Tk()
window.title("Flashy")
window.config(pady=50,padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
flashcard_img = PhotoImage(file="images/card_front.png")
canvas.create_image(526,800, image=flashcard_img)
flashcard_top_txt = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)



window.mainloop()