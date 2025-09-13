from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake!")

snake = Snake()
food = Food()

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

        screen.ontimer(game_loop, 100)

game_loop()
screen.exitonclick()