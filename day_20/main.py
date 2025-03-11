from snake import *

sc = Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")


run = True
while run:
    sc.update()
    sleep(0.1)
    snake.snake_move()



sc.exitonclick()