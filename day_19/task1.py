from turtle import Turtle,Screen

t = Turtle()
screen = Screen()


t.pensize(3)

def move_forward():
    t.forward(10)
def move_backward():
    t.backward(10)
def turn_left():
    new_heading = t.heading()+10
    t.setheading(new_heading)
def turn_right():
    t.rt(10)
def clear():
    t.reset()
    t.pensize(3)

screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=turn_left,key="a")
screen.onkey(fun=turn_right,key="d")
screen.onkey(fun=clear,key="c")





screen.exitonclick()