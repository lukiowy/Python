from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        self.color("white")
        self.up()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def inc_speed(self):

        self.y_move += 2     

    def wall_bounce(self):
        self.y_move *= -1
    
    def paddle_bounce(self):
        if self.xcor() > 320:
            self.x_move += 5
        elif self.xcor() < -320:
            self.x_move -= 5
        self.x_move *= -1
    
    def restart(self):
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.paddle_bounce()
        