from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_keeping()

    def score_keeping(self):

        self.write("Score:", move=True, align='center', font=('Arial', 10, 'normal'))
