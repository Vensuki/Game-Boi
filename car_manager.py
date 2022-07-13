COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import turtle
import random
import time


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(280, new_y)
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2)
            self.all_cars.append(new_car)


    def move(self):
        for i in self.all_cars:
            i.forward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
