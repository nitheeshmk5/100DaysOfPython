import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move,"Up")

cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    #collision with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.gameOver()

    #finised
    if player.finished():
        player.go_to_start()
        cars.level_up()
        score.increase_lvl()

screen.exitonclick()