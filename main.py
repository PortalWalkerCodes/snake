from turtle import Turtle, Screen
import time

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake!")
segments = []

x_cor = 0

for _ in range(3):
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(x=x_cor, y=0)
    x_cor -= 20
    segments.append(new_segment)
screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x=new_x, y=new_y)
    segments[0].forward(20)





screen.exitonclick()