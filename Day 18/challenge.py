from turtle import Turtle, Screen
import random

betty = Turtle()

colours = ['black', 'red', 'green', 'yellow', 'blue']

screen = Screen()
# making the turtles nib bigger
betty.pensize(10)
betty.speed(0)

moves = [90, 180, 270, 0]

for _ in range(500):
    betty.color(random.choice(colours))
    # betty.pencolor("red)
    betty.forward(30)
    betty.setheading(random.choice(moves))

screen.exitonclick()
