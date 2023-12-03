from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
guess = screen.textinput(title="Make your bet",prompt="Choose color of turtle: ")
colors = ["red","orange","yellow","green","blue","purple"]
x = -230
y = -100
turtles = []
for i in range(len(colors)):
    turt = Turtle(shape="turtle")
    turt.color(colors[i])
    turt.up()
    turt.goto(x=x, y=y)
    y += 40
    turtles.append(turt)

if guess:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning = turtle.color()
            if winning == guess:
                print("You won!")
            else:
                print(f"You lost, {winning} color won!")
        speed = random.randint(0,10)
        turtle.forward(speed)
        
        

screen.exitonclick()