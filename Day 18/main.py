# import colorgram
# rgb = []
# colors = colorgram.extract('C:\Python\Day 18\image.jpg', 16)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb.append(new_color)
# print(rgb)
color_list = [(171, 158, 33), (99, 6, 51), (75, 94, 173), (232, 209, 73), (10, 35, 127), (178, 104, 155), (215, 89, 34), (105, 123, 210), (26, 96, 40), (33, 103, 47), (242, 237, 240), (113, 131, 212), (184, 116, 161), (218, 92, 40), (232, 235, 244)]
import turtle as t
from turtle import Screen
import random
t.colormode(255)

def random_color():
    rand_col = random.choice(color_list)
    return rand_col

turt = t.Turtle()
x = -200
y = -220
turt.speed(20)
turt.hideturtle()

for i in range(10):
    turt.up()
    turt.goto(x,y)
    y +=40
    for j in range(10):
        turt.down()
        turt.dot(20, random_color())
        turt.up()
        turt.forward(50)

screen = Screen()
screen.exitonclick()