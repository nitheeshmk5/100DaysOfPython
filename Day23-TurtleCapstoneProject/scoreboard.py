from turtle import Turtle

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-275,260)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}",align='left',font=FONT)
    
    def increase_lvl(self):
        self.level += 1
        self.update_score()

    def gameOver(self):
        self.goto(0,0)
        self.write("Game over",align='center',font=FONT)

