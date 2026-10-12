from turtle import Turtle, Screen
pen = Turtle()
screen = Screen()
def move_forward():
    pen.forward(20)

def move_backward():
    pen.backward(20)

def turn_left():
    new_heading = pen.heading() + 10
    pen.setheading(new_heading)

def turn_right():
    new_heading = pen.heading() - 10
    pen.setheading(new_heading)

def home():
    pen.penup()
    pen.setx(0)
    pen.sety(0)
    pen.pendown()

def clear():
    pen.clear()
    home()

#first we need to listen to events then we can react to it
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
print(pen.heading())
screen.exitonclick()
