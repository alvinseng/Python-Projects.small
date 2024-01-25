import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    # player movement
    if player.ycor() > 280:
        score.score_keeping()
        player.spawn()

    # Cars movement from right to left
    if car.xcor() != -320:
        car.car_move()

    if player




