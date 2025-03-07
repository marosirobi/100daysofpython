# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

names = ["Pikachu","Squirtle","Charmander"]
types = ["Electric","Water","Fire"]

table.add_column("Pokemon Name",names,)
table.add_column("Type",types)
table.align = "l"

print(table)
