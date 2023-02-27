import turtle

import colorgram
from turtle import Turtle, Screen
import random
turtle.colormode(255)
# colors = colorgram.extract("img.jpg", 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

colors_list = [(141, 176, 176), (25, 32, 32), (28, 105, 105), (208, 161, 161), (238, 222, 222), (230, 211, 211),
               (131, 31, 31), (5, 162, 162), (182, 45, 45), (217, 60, 60), (226, 80, 80), (195, 129, 129),
               (54, 167, 167), (29, 61, 61), (108, 181, 181), (109, 99, 99), (2, 102, 102), (193, 187, 187),
               (241, 204, 204), (19, 22, 22), (52, 149, 149), (171, 211, 211), (226, 170, 170), (150, 207, 207),
               (234, 169, 169), (184, 186, 186), (115, 38, 38)]
tim = Turtle()
tim.penup()
tim.speed(0)
tim.hideturtle()

def reset_home():
    tim.goto(-250, -250)


def row_10_dots_forwards():
    reset_home()
    move_up(row)
    for _ in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)



def move_up(row):
    tim.left(90)
    tim.forward(50 * row)
    tim.right(90)


for row in range(10):
    row_10_dots_forwards()













turtle.exitonclick()
