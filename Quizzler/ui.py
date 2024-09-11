from tkinter import *

FONT_NAME = "Arial"
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz = self.canvas.create_text(
            150,
            125,
            text="Some text questions",
            fill="black",
            font=(FONT_NAME, 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2)

        correct = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct, highlightthickness=0)
        self.correct_button.grid(column=0, row=2)





        self.window.mainloop()