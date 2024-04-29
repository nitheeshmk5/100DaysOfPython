from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.new_turtle = []
        self.create_snake()
        self.head = self.new_turtle[0]
    
    def create_snake(self):
        for position in POSITIONS:
            self.add_new(position)
            
    def add_new(self,pos):
        my_turtle = Turtle('square')
        my_turtle.color("skyblue")
        my_turtle.penup()
        my_turtle.goto(pos)
        self.new_turtle.append(my_turtle)
        
    
    def extend(self):
        self.add_new(self.new_turtle[-1].position())

    def move(self):
        for n in range(len(self.new_turtle) - 1,0,-1):
            new_x = self.new_turtle[n-1].xcor()
            new_y = self.new_turtle[n-1].ycor()
            self.new_turtle[n].goto(new_x,new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    
    


