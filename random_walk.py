import turtle as t
import random
tim = t.Turtle()
my_screen = t.Screen()
my_screen.canvwidth = 3000
my_screen.canvheight = 3000
colors = ["royal blue", "gold", "red", "dark magenta", "midnight blue", "orange red"]
direction = [0, 90, 180, 270]
count = 0
tim.speed(0)
tim.pensize(10)
while count<100:
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))

#    random.choice(movement)
    count +=1


my_screen.exitonclick()