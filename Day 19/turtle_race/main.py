from turtle import Turtle, Screen, TK
import random
screen = Screen()

screen.setup(500, 400)
colors = ["red", "green", "blue", "yellow", "purple", "indigo"]
user_bet = screen.textinput("chose color", "On which turtle would you like bet?\nRed,Green,Blue,Yellow,Purple,Indigo")
y_position = [-70,-40,-10,20,50,80]
all_turtles = []
for i in range(6):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(-230,y_position[i])
    all_turtles.append(turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet.lower() == winner.lower():
                print("You Win!")
                TK.messagebox.showinfo(title="You win", message=f"You Win!,You bet correctly the winner is {winner}")

            else:
                print(f"You Lose!, The winner is {winner}")
                TK.messagebox.showinfo(title="You lose", message=f"You Lose!, The winner is {winner}")

        random_distance=random.randint(1,10)
        turtle.forward(random_distance)

screen.exitonclick()