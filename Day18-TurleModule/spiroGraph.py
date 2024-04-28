from turtle import Turtle,Screen
from random import choice,randint
import turtle as t

my_turtle = Turtle()
t.colormode(255)


my_turtle.shape("turtle")
my_turtle.speed("fastest")

def draw(n):
    for _ in range(n):
        colors = (randint(0,255),randint(0,255),randint(0,255))
        my_turtle.color(colors,colors)
        my_turtle.circle(100)
        current_heading = my_turtle.heading()
        my_turtle.setheading(current_heading + 5)

draw(200)
#Screen
my_screen = Screen()
my_screen.exitonclick()