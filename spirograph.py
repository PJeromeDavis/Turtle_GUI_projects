import turtle as t
import random
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
#colors = ["royal blue", "gold", "red", "dark magenta", "midnight blue", "orange red"]
tim.speed(0)
angle = 166
count = 0
#while angle <= 360:   #for making circle
#    tim.left(angle)
#    tim.circle(100)
#    angle += 1
#    tim.color(random_color())
while count <= 360:   #for making spiro
     tim.forward(300)
     tim.left(angle)

     count += 1
     tim.color(random_color())




my_screen.exitonclick()
