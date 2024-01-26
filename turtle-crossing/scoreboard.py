from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level = 1
        self.goto(-260,260)
        self.crossing_level()

    def crossing_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def score_keeping(self):
        self.level += 1
        self.crossing_level()

    def car_collision(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)

