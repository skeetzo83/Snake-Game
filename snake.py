import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.alona_snake = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            alona = Turtle(shape="square")
            alona.color("white")
            alona.penup()
            alona.goto(position)
            self.alona_snake.append(alona)

    def move(self):
        for seg_num in range(len(self.alona_snake) - 1, 0, -1):
            new_x = self.alona_snake[seg_num - 1].xcor()
            new_y = self.alona_snake[seg_num - 1].ycor()
            self.alona_snake[seg_num].goto(new_x, new_y)
        self.alona_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.alona_snake[0].heading() != DOWN:
            self.alona_snake[0].setheading(UP)

    def left(self):
        if self.alona_snake[0].heading() != RIGHT:
            self.alona_snake[0].setheading(LEFT)

    def right(self):
        if self.alona_snake[0].heading() != LEFT:
            self.alona_snake[0].setheading(RIGHT)

    def down(self):
        if self.alona_snake[0].heading() != UP:
            self.alona_snake[0].setheading(DOWN)


    def add_tail(self, position):
        alona = Turtle(shape="square")
        alona.color("white")
        alona.penup()
        alona.goto(position)
        self.alona_snake.append(alona)


    def reset(self):
        for seg in self.alona_snake:
            seg.goto(1000, 1000)
        self.alona_snake.clear()
        self.create_snake()
    def extend(self):
        self.add_tail(self.alona_snake[-1].position())



