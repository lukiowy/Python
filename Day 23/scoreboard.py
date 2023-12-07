from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("black")
        self.goto(-270, 250)
        self.hideturtle()
        self.level = 1
        self.write(f"Level: {self.level}", font=FONT)

    def add_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(x=-90,y=0)
        self.write("Game over.", font=FONT)
