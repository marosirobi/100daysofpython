from datetime import time
from time import sleep
from turtle import Turtle,Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.snake_default_body()
        self.head = self.snake[0]
    def snake_default_body(self):
        x=0
        y=0
        for body in range(3):
            body = Turtle("square")
            body.penup()
            body.color("white")

            x -= 20
            body.teleport(x,y)
            self.snake.append(body)

    def snake_eat(self):
        pass

    def snake_move(self):
        for body in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body - 1].xcor()
            new_y = self.snake[body - 1].ycor()
            self.snake[body].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
