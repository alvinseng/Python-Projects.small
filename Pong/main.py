from turtle import Screen
from paddle import Paddle
from score import Scoreboard
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
score = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

p1_score = score.player_score((300, 260))
p2_score = score.player_score((-300, 260))


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    score.scoreboard_update()
    r_paddle
    l_paddle
    p1_score
    p2_score



screen.exitonclick()