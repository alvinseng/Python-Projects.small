import time
import turtle
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
    car.create_car()
    car.move()

    # successful crossing
    if player.at_finishline() == True:
        player.go_to_start()
        car.level_up()
        score.score_keeping()

    # detect collision
    for c in car.new_car:
        if c.distance(player) < 20:
            score.car_collision()
            game_is_on = False






screen.exitonclick()



