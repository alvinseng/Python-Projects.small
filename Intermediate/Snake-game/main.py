from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_pos = [(0,0), (-20,0), (-40,0)]

segments = []

for snake_body in snake_pos:
  new_snake = Turtle(shape = "square")
  new_snake.color("white")
  new_snake.pu()
  new_snake.goto(snake_body)
  segments.append(new_snake)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    for seg_num in range(start = ,stop = , step = ):
