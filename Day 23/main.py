from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # detcet collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False
    if player.has_finished():
        player.starting_position()
        scoreboard.increase_level()
        car_manager.level_up()

screen.exitonclick()
