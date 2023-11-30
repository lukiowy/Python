# import turtle

# asd = turtle.Turtle()
# asd.shape("turtle")
# asd.color("red")
# my_screen = turtle.Screen()
# asd.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([["Pikachu", "Electric"],["Squirtle", "Water"],["Charmander", "Fire"]])
table.add_column("Pokemon Names", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "FIre"])
table.align = "l"
print(table)