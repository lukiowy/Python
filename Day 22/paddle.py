from turtle import Turtle
SIZE_X = 5
SIZE_Y = 1
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.shape("square")
        self.color("white")
        self.up()
        self.shapesize(SIZE_X,SIZE_Y)

    def move_up(self):
        self.y +=20
        self.goto(self.x, self.y)

    def move_down(self):
        self.y -=20
        self.goto(self.x, self.y)


