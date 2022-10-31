from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

game_is_on = True
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

scr.listen()
scr.onkey(fun=snake.up, key="Up")
scr.onkey(fun=snake.down, key="Down")
scr.onkey(fun=snake.right, key="Right")
scr.onkey(fun=snake.left, key="Left")

while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    #  Detect collision with food
    if snake.head.distance(food) < 15:
        food.food_location()
        snake.extend()
        scoreboard.score_up()

    #  Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset()
        snake.reset()

    #  Detect collision with tail
    for tail in snake.segments[1:]:
        if snake.head.distance(tail) < 10:
            scoreboard.reset()
            snake.reset()


scr.exitonclick()
