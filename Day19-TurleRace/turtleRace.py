from turtle import Turtle,Screen
from random import choice
import turtle as t

t.title("Turtle race")

my_screen = Screen()
my_screen.setup(width=800,height=500)
race = False
user_input = my_screen.textinput("Make you bet ","Enter the color of the turtle you think that will win \n(red,green,skyblue,pink,yellow,violet,orange) : ")

colors = ['red','green','skyblue','pink','yellow','violet',"orange"]
y_axis = [-150,-100,-50,0,50,100,150]
movement = [5,10,15,5,10,3,9,8,14]
all_turtle = []

if user_input:
    race = True
    line = Turtle()
    line.penup()
    line.goto(x=350,y=175)
    line.color("red","black")
    line.pendown()
    line.right(90)
    line.forward(350)
    line.hideturtle()

    for t in range(7):
        tur = Turtle()
        tur.shape("turtle")
        tur.penup()
        tur.goto(x=-350,y=y_axis[t])
        tur.color(colors[t])
        all_turtle.append(tur)


while race:
    for tur in all_turtle:
        tur.forward(choice(movement))
        if tur.xcor() > 330:
            winner_color = tur.pencolor()
            if winner_color == user_input:
                print("Congratulations! You won!")
            else:
                print("Oops, You lose!")
            winner = winner_color  
            race = False 
            if winner:
                print("RACE RESULTS 🏁")
                print(f"🏆 {winner}")
                break


my_screen.exitonclick()