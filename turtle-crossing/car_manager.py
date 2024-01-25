from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.new_car = []

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.new_car.append(new_car)

    def move(self):
        for car in self.new_car:
            car.backward(STARTING_MOVE_DISTANCE)


