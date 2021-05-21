import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.bgcolor("grey")
screen.bgpic("bg.gif")
screen.setup(width=1400, height=800)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for i in car_manager.all_cars:
        if i.distance(player) < 30:
            player.reset()
            car_manager.reset()
            scoreboard.reset_score()
            scoreboard.update_scoreboard()
            car_manager.reset()

        if player.ycor() > 398:
            scoreboard.inc_score()
            player.reset()
            car_manager.lvl -= 1
            car_manager.level_up()
