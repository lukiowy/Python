from turtle import Turtle, Screen
import random

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x = 0, y = 250)
        with open("C:\Python\Day 24\data.txt") as f:
            self.high_score = int(f.read())
        self.score = 0
        self.up()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.update()

    def add(self):
        self.score +=1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move = False, align ="center", font=("Arial", 20, "normal"))
    #def game_over(self):
    #    self.goto(x = 0, y = 0)
    #    self.write("Game over.", move = False, align ="center", font=("Arial", 15, "normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:\Python\Day 24\data.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update()