from turtle import Turtle
ALIGNMENT = "center"
P1_ALIGNMENT = "right"
P2_ALIGNMENT = "left"
SCORE_FONT = ('Courier', 20, 'normal')
PLAYER_FONT = ('Courier', 55, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.player_score()

    def player_score(self):
        self.clear()
        self.goto(165, 220)
        self.write(f"{self.r_score}",align=ALIGNMENT, font=PLAYER_FONT)
        self.goto(-165, 220)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=PLAYER_FONT)

    def l_point(self):
        self.l_score += 1
        self.player_score()

    def r_point(self):
        self.r_score += 1
        self.player_score()