import turtle as t
import random
timmy = t.Turtle()
my_screen = t.Screen()
my_screen.canvwidth
colors = ["royal blue", "lime", "gold", "red"]
timmy.shape("turtle")
angle = 120
sides = 3
while angle >= 36 :
    timmy.color(random.choice(colors))
    for round in range(sides):
        timmy.forward(100)
        timmy.right(angle)
    sides += 1
    angle = 360/sides

my_screen.exitonclick()