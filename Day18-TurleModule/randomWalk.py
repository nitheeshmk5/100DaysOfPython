from turtle import Turtle,Screen
from random import choice,randint
import turtle as t

my_turtle = Turtle()
t.colormode(255)


my_turtle.shape("turtle")
direction = [0,90,180,270]
my_turtle.pensize(15)
my_turtle.speed("fastest")

def draw(n):
    for _ in range(n):
        colors = (randint(0,255),randint(0,255),randint(0,255))
        my_turtle.color(colors,colors)
        my_turtle.forward(30)
        my_turtle.setheading(choice(direction))

draw(200)
#Screen
my_screen = Screen()
my_screen.exitonclick()