from turtle import Turtle,Screen

my_turtle = Turtle()
my_turtle.shape("turtle")

def move_forward():
    my_turtle.forward(15)

def move_backward():
    my_turtle.back(15)

def move_right(): 
    my_turtle.right(10)


def move_left():
    left = my_turtle.heading() + 10
    my_turtle.setheading(left)
    #my_turtle.left(10)

def clear():
    '''It clears everything on the screen'''
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

my_screen = Screen()
my_screen.listen()
my_screen.onkey(key="w",fun=move_forward)
my_screen.onkey(key="Up",fun=move_forward)
my_screen.onkey(key="s",fun=move_backward)
my_screen.onkey(key="Down",fun=move_backward)
my_screen.onkey(key="d",fun=move_right)
my_screen.onkey(key="Right",fun=move_right)
my_screen.onkey(key="a",fun=move_left)
my_screen.onkey(key="Left",fun=move_left)
my_screen.onkey(key="c",fun=clear)
my_screen.onkey(key="1",fun=clear)

my_screen.exitonclick()