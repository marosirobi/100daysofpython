from snake import *
from food import *
from scoreboard import *

sc = Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #detect collision
    if snake.head.distance(food) < 15:
        snake.snake_grow()
        food.refresh()
        scoreboard.increase_score()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        run = False
    if snake.snake_over():
        scoreboard.game_over()
        run = False

sc.exitonclick()