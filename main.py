import turtle
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
snake_score = 0

scoreboard
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


snake.create_snake()
game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.alona_snake[0].distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.add_score()


    #detect wall collision
    if snake.alona_snake[0].xcor() < -280 or snake.alona_snake[0].xcor() > 280 or snake.alona_snake[0].ycor() > 280 or snake.alona_snake[0].ycor() < -280:
        scoreboard.game_over()
        snake.reset()
    for tail in snake.alona_snake[1:]:
        if snake.alona_snake[0].distance(tail) < 10:
            scoreboard.game_over()









screen.exitonclick()