from importlib.metadata import pass_none
from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake!")
turtles = []

x_cor = 0

for _ in range(3):
    new_turtle = Turtle("square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(x=x_cor, y=0)
    x_cor -= 20
    turtles.append(new_turtle)





screen.exitonclick()