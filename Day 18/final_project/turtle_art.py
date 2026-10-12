from turtle import Turtle, Screen
import random
screen = Screen()
art = Turtle()
color_list = ['#d4955f', '#d7503e', '#2f5e8e',
              '#e7da5c', '#94425b', '#161b28',
              '#9b493c', '#7aa7c3', '#28161d',
              '#27130f', '#d14659', '#c08c9f',
              '#27835b', '#7db38d', '#4ba460',
              '#e5a9b7', '#0f1f16', '#333766',
              '#e9dc0c', '#9fb136', '#632c3f',
              '#23a4c4', '#eaaba2', '#692c27',
              '#a4d1bb', '#97cedc']
art.speed("fastest")
art.setheading(225)
art.penup()
art.forward(300)
art.setheading(0)

def draw():
    for _ in range(10):
        art.dot(20,random.choice(color_list))
        art.penup()
        art.forward(50)
        art.pendown()

    art.setheading(90)
    art.penup()
    art.forward(50)
    art.setheading(180)
    art.forward(500)
    art.setheading(360)

for i in range(10):
    draw()
art.hideturtle()
screen.exitonclick()
