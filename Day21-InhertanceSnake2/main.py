from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score

my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("SNAKE game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.left,"Left")




gameOn = True
while gameOn:
    my_screen.update()
    time.sleep(0.2)
    snake.move()

    #collision
    if snake.head.distance(food) < 15:
        food.new_food()
        score.point()
        snake.extend()

    #wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameOn = False
        score.game_over()

    #tail
    for tur in snake.new_turtle[1:]:
        if snake.head.distance(tur) < 10:
            gameOn = False
            score.game_over()
            

    
my_screen.exitonclick()