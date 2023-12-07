from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        #self.create_car()
        #self.move()

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)
        print(self.speed)
        
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 3:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.up()
            random_y = random.randint(-250,250)
            car.shapesize(1, 2)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def increase_speed(self):
        self.speed = MOVE_INCREMENT + STARTING_MOVE_DISTANCE