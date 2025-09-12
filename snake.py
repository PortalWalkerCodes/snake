from turtle import Turtle

MOVE_DISTANCE = 20
class Snake:
    def __init__(self):

        self.segments = []
        self.x_cor = 0
        self.create_snake()
        self.head = self.segments[0]
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0

    def create_snake(self):
        for _ in range(3):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=self.x_cor, y=0)
            self.x_cor -= 20
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)