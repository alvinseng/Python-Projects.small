from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_design()
        self.goto(300,0)
        self.seth(180)

    def car_design(self):
        self.shape("square")
        self.pu()
        car_color = random.choices(COLORS)
        self.color(car_color)


    def car_move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        new_y = self.ycor()
        self.goto(new_x, new_y)