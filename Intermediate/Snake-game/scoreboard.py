from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 270)
        self.scoreboard_update()

    def scoreboard_update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def score_keeping(self):
        self.score += 1
        self.clear()
        self.scoreboard_update()

