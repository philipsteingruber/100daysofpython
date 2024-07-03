import random
from turtle import Turtle, Screen

import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

turtle = Turtle()
screen = Screen()
screen.colormode(255)

turtle.pensize(25)
turtle.speed(0)
turtle.penup()

step = 50

turtle.sety(step)
turtle.setx(step)
for i in range(10):
    turtle.sety(step * (i+1))
    for j in range(10):
        turtle.dot(25, random.choice(rgb_colors))
        turtle.setx(step * (j+1))


screen.exitonclick()
