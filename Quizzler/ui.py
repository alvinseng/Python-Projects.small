from tkinter import *
from quiz_brain import QuizBrain

FONT_NAME = "Arial"
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text questions",
            fill="black",
            font=(FONT_NAME, 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0, command=self.answer_wrong)
        self.wrong_button.grid(column=1, row=2)

        correct = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct, highlightthickness=0, command=self.answer_correct)
        self.correct_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def answer_correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
