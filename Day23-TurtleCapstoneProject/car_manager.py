from turtle import Turtle
from random import randint,choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    
    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 5:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(350,randint(-250,250))
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
    
    def level_up(self):
        self.speed += MOVE_INCREMENT



    
