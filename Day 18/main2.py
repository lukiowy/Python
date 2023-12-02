from turtle import Screen
import turtle as t
import random
maciek = t.Turtle()
maciek.shape("turtle")
maciek.color("red")
#challenge 1
# for i in range(4):
#     maciek.forward(100)
#     maciek.right(90)
#challenge 2
# for i in range(15):
#     maciek.forward(10)
#     maciek.up()
#     maciek.forward(10)
#     maciek.down()
#challenge 3
# for i in range(3):
#     maciek.forward(100)
#     maciek.right(120)
# for i in range(4):
#     maciek.color("blue")
#     maciek.forward(100)
#     maciek.right(90)
# for i in range(5):
#     maciek.color("green")
#     maciek.forward(100)
#     maciek.right(72)
# for i in range(6):
#     maciek.color("cyan")
#     maciek.forward(100)
#     maciek.right(60)
# for i in range(7):
#     maciek.color("black")
#     maciek.forward(100)
#     maciek.right(51.5)
# for i in range(8):
#     maciek.color("DarkViolet")
#     maciek.forward(100)
#     maciek.right(45)
# for i in range(9):
#     maciek.color("DeepPink")
#     maciek.forward(100)
#     maciek.right(40)
# for i in range(10):
#     maciek.color("gray30")
#     maciek.forward(100)
#     maciek.right(36)
#challenge 4
# maciek.width(5)
# maciek.speed(10)
t.colormode(255)
# colors = ["red", "blue", "green", "black", "magenta"]
# direct = ["0", "90", "180", "270"]
def col():
     r = random.randint(0,255)
     g = random.randint(0,255)
     b = random.randint(0,255)
     rgb = (r,g,b)
     return rgb
# def direction():
#     return random.choice(direct)
# for i in range (50):
#     maciek.forward(100)
#     maciek.right(int(direction()))
#     maciek.color(col())
#challenge 5
print(col())
maciek.speed(20)
for i in range(72):
    maciek.color(col())
    maciek.circle(100)
    maciek.right(5)
screen = Screen()
screen.exitonclick()