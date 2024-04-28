from turtle import Turtle,Screen
from random import choice

my_turtle = Turtle()
my_turtle.shape("turtle")

colors = ['red','skyblue','orange','green','violet','purple','pink']
def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for n in range(3,10):
    my_turtle.color(choice(colors))
    draw_shape(n)


#Screen
my_screen = Screen()
my_screen.exitonclick()