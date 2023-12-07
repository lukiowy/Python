from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def next_level(self):
        self.goto(STARTING_POSITION)
        #self.create_player()
    
    def create_player(self):
        self.color("green")
        self.shape("turtle")
        self.left(90)
        self.up()
        self.goto(STARTING_POSITION)