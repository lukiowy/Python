import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")
screen.onkey(screen.bye, "Escape")

game_is_on = True

while game_is_on:
    car.create_car()
    car.move()
    time.sleep(0.1)

    if player.ycor() > 250:
        player.next_level()
        score.add_score()
        car.increase_speed()
        
    for cars in car.all_cars:
        if player.distance(cars) < 25:
            score.game_over()
            game_is_on = False
    screen.update()

screen.exitonclick()
