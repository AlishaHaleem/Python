import time
from turtle import Screen
from player import Player
# TODO;
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager() #TODO

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
