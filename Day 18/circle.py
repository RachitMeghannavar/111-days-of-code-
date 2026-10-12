from turtle import Turtle, Screen
import random
screen = Screen()
turtle = Turtle()
turtle.speed(0)
colors = ["red", "blue", "green", "yellow", "cyan", "magenta"]
for j in range(72):
    for i in range(4):
        turtle.color(random.choice(colors))
        turtle.forward(100)
        turtle.left(90)
    turtle.left(5)



screen.exitonclick()