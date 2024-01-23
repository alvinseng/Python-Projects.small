from turtle import Turtle
ALIGNMENT = "center"
P1_ALIGNMENT = "right"
P2_ALIGNMENT = "left"
SCORE_FONT = ('Courier', 18, 'normal')
PLAYER_FONT = ('Courier', 24, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.scoreboard_update()
        self.player_score()

    def scoreboard_update(self):
        self.goto(0, 240)
        self.write(f"Score \n{self.p2_score} | {self.p1_score}", align=ALIGNMENT, font=SCORE_FONT)

    def player_score(self, position):
        self.goto(position)
        self.write("P1",align=ALIGNMENT, font=PLAYER_FONT)
