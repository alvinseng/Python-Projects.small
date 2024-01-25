from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        car_color = random.choices(COLORS)
        self.pu()
        self.goto(300,0)
        self.shape("square")
        self.color(car_color)
        self.turtlesize(stretch_wid=1, stretch_len=2)

    def random_start(self):
        self.goto(0, 300)
        # for _ in range(0, 300):
        #     self.create_car()

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        random_y = random.randint(-240,240)
        self.goto(new_x, random_y)

