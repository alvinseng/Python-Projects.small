from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")


snake_pos = [(0,0), (-20,0), (-40,0)]

for snake_body in snake_pos:
  new_snake = Turtle(shape = "square")
  new_snake.color("white")
  new_snake.goto(snake_body)
