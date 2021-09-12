from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.color(choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, randint(-240, 240))
            self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.backward(self.speed)


    def increaseSpeed(self):
        self.speed += MOVE_INCREMENT

