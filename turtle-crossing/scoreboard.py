from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.goto(-240,260)
        self.hideturtle()
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def score_keeping(self):
        self.score += 1
        pass
