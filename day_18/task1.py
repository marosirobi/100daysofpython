import turtle
from random import random
from turtle import Turtle, Screen
import random
# import heroes,villains
# print(heroes.gen())
# print(villains.gen())

directions = [0,90,180,270]

# def draw(sides):
#     angle = 360 / sides
#
#     t.color(random.choice(colors))
#     for i in range(sides):
#         t.fd(100)
#         t.rt(angle)



t = Turtle()
turtle.colormode(255)
screen = Screen()
# for i in range(3,11):
#     draw(i)

def r_color():
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.color(random_color)

def circle(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        r_color()
        t.speed("fastest")
        t.setheading(t.heading() + size_of_gap)
        t.circle(100)


circle(4)

screen.exitonclick()





