from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level = 0
        self.crossing_level()

    def crossing_level(self):
        self.clear()
        self.goto(-240,260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def score_keeping(self):
        self.level += 1
        self.crossing_level()

    def car_collision(self):
        self.write("Game Over", align="center", font=FONT)

