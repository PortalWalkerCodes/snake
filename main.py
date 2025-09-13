from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake!")


screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

def game_loop():
    if game_is_on:
        screen.update()
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.update_score()

        screen.ontimer(game_loop, 100)

game_loop()
screen.exitonclick()