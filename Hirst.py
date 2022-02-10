import turtle as t
import random
import colorgram
t.colormode(255)
def random_color():
    r = random.choice(range(255))
    g = random.choice(range(255))
    b = random.choice(range(255))
    return (r, g, b)
tim = t.Turtle()
my_screen = t.Screen()
my_screen.canvwidth = 3000
my_screen.canvheight = 3000
tim.penup()
x = -200
y = -200

while y != 100:
    tim.setposition(x, y)
    while x != -100:
        tim.dot(10, random_color())

        tim.forward(50)
        x += 10
    x = -200
    y += 50


my_screen.exitonclick()