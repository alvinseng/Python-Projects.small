from turtle import Screen
from paddle import Paddle
from score import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
score = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    r_paddle
    l_paddle
    score.player_score()
    ball.move()

    #detect collision to wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when R paddles misses
    if ball.xcor() > 380:
        ball.ball_reset()
        score.l_point()

    # detect when L paddles misses
    if ball.xcor() < -380:
        ball.ball_reset()
        score.r_point()





screen.exitonclick()