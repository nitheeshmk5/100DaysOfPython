from turtle import Turtle,Screen
import turtle as t
from random import choice

t.colormode(255)
my_turtle = Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()

color_list = [(249, 17, 228), (213, 9, 13), (198, 35, 12), (231, 5, 228), (197, 20, 69), (33, 188, 90), (43, 71, 212), (234, 40, 148), (33, 152, 30), (16, 55, 22), (66, 49, 9), (240, 251, 245), (244, 149, 39), (65, 229, 202), (14, 222, 205), (63, 10, 21), (224, 111, 19), (229, 8, 165), (15, 22, 154), (245, 16, 58), (98, 9, 75), (248, 9, 11), (222, 203, 140), (68, 161, 240), (10, 62, 97), (5, 33, 38), (68, 155, 219), (238, 212, 157), (86, 208, 77), (86, 235, 225), (250, 14, 8), (242, 157, 166), (177, 224, 180), (36, 159, 243), (6, 115, 81), (11, 248, 55)]

my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

for dot in range(1,101):
    my_turtle.dot(20,choice(color_list))
    my_turtle.forward(50)

    if dot % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)


my_screen = Screen()
my_screen.exitonclick()