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

car_spawn = car.create_car()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    # player movement
    if player.ycor() > 280:
        score.score_keeping()
        player.spawn()

    # for _ in range(6):
    #     car_spawn

    # Cars movement from right to left
    if car.xcor != -300:
        car.create_car()

    # if player




