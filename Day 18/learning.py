from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
pen.color("white")
pen.forward(100)
screen.exitonclick()