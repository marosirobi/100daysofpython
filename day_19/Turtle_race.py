from turtle import Turtle,Screen
import random

def creating_turtles(x_pos,y_pos,all_t):
    for turtle in range(6):
        t = Turtle(shape="turtle")
        t.color(colors[turtle])
        t.penup()
        t.goto(x=x_pos, y=y_pos)
        y_pos += 50
        all_t.append(t)

sc = Screen()

sc.setup(width=500, height=400)
usr_bet = sc.textinput(title="Make your bet",prompt="Which turtle will win the race? enter a color: ")
colors = ['red','blue','green','yellow','orange','purple']
all_t = []

x_pos = -230
y_pos = -130
t = Turtle()
t.hideturtle()

creating_turtles(x_pos,y_pos,all_t)

is_race_on = False

if usr_bet:
    is_race_on = True

while is_race_on:
    random_turtle = random.choice(all_t)

    if random_turtle.xcor() > 230:
        winning_color = random_turtle.pencolor()
        is_race_on = False
        if winning_color ==usr_bet:
            print(f"You won! {winning_color}!")
        else:
            print(f"You lost! {winning_color}!")

    random_distance = random.randint(0,10)
    random_turtle.forward(random_distance)




sc.exitonclick()