from turtle import Turtle
ALIGNMENT = "center"
P1_ALIGNMENT = "right"
P2_ALIGNMENT = "left"
SCORE_FONT = ('Courier', 20, 'normal')
PLAYER_FONT = ('Pixel', 75, 'bold')


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.player_score(position)

    def player_score(self, position):
        self.goto(position)
        self.write(f"{self.score}",align=ALIGNMENT, font=PLAYER_FONT)
