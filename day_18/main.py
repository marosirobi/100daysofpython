# import colorgram
# colors = colorgram.extract('image.png',30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b) #tupple
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle
import random
from turtle import Turtle,Screen
color_list = [(199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (108, 68, 84), (113, 161, 175), (40, 37, 35), (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53), (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152), (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171), (169, 200, 209), (205, 183, 188), (41, 75, 61), (148, 116, 122), (39, 72, 81), (97, 138, 153)]
t = Turtle()
screen = Screen()
turtle.colormode(255)

x = -t.getscreen().canvwidth
y = -t.getscreen().canvheight

t.teleport(x,y)
t.speed("fastest")
def square(x,y,num_dotes):

    h = 400
    w = 300
    for j in range(num_dotes):
        for i in range(num_dotes):
            t.color(random.choice(color_list))
            t.dot(20)
            t.teleport(x,y)
            x+=50
        y+=50
        x = -h
    t.color(random.choice(color_list))
    t.dot(20)

square(x,y,9)

screen.exitonclick()