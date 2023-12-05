from turtle import Turtle, Screen
import random

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x = 0, y = 250)
        self.score = 0
        self.up()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.add()

    def add(self):
        self.clear()
        self.write(f"Score: {self.score}", move = False, align ="center", font=("Arial", 20, "normal"))
        self.goto(x = 0, y = 250)
        self.score +=1

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write("Game over.", move = False, align ="center", font=("Arial", 15, "normal"))