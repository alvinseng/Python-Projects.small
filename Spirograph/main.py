import turtle as t
import random

tt = t.Turtle()
ts = t.Screen()
rand = random

"""Turtle style and config"""
tt.shape("circle")
tt.hideturtle()
tt.pensize(1)
ts.colormode(255)

def random_color():
    R = rand.randint(0,255)
    G = rand.randint(0, 255)
    B = rand.randint(0, 255)
    random_color = (R, G, B)
    return random_color


for _ in range(200):
    # tt.forward(30)
    tt.circle(100)
    tt.pencolor(random_color())














"""Screen style and config"""
ts.exitonclick()
