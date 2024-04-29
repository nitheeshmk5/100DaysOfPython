from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.go_to_start()
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else: return False
    
    def go_to_start(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

