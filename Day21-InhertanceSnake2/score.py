from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.write(f"Score : {self.score}",align='center',font=('Courier',22,'normal'))
        self.hideturtle()
    
    def point(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}",align='center',font=('Courier',22,'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over !",align='center',font=('Arial',22,'normal'))
        
        
        