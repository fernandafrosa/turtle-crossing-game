import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Fernanda´s Turtle Crossing Game")
screen.tracer(0)

#TODO: Initialize components
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")



game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    #turtle crosses the screen
    if player.ycor() > 280:
        scoreboard.scorePoint()
        scoreboard.updateLevel()
        player.initializePos()
        #cars need to have its speed increased



screen.exitonclick()