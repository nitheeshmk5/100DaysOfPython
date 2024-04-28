from turtle import Turtle,Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("orange","red")

def square():
    i = 0
    while i <= 3:
        my_turtle.forward(100)
        my_turtle.right(90)
        i += 1

square()
my_screen = Screen()
my_screen.exitonclick()