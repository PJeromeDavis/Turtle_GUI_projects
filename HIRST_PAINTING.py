#import colorgram
#colors = colorgram.extract('image.jpg', 10)
#colors_list = []
#for _ in colors:  #here the loop goes thru color object
#    rgb = _.rgb  #here colors contain a list of objects having a attribute called "rgb" where "rgb" itself is
#    # object containing attributes named "r" "g" "b"
#    r = rgb.r
#    g = rgb.g
#    b = rgb.b
#    color_code = (r, g, b)
#    colors_list.append(color_code)
import turtle as t
import random
colors_list = [(232, 229, 220), (226, 161, 72), (45, 102, 148), (116, 165, 193), (155, 63, 88), (191, 162, 30),
               (26, 135, 95), (201, 133, 154), (167, 79, 47), (216, 87, 57)]
t.colormode(255)
#def random_color():
#    r = random.choice(range(255))
#    g = random.choice(range(255))
#    b = random.choice(range(255))
#    return (r, g, b)
tim = t.Turtle()
my_screen = t.Screen()
my_screen.canvwidth = 500
my_screen.canvheight = 500
#print(my_screen.canvheight)
tim.penup()
x = -250
y = -250

while y != 250:
    tim.setposition(x, y)
    while x != 250:
        turtle_color = random.choice(colors_list)
        tim.dot(20, turtle_color)
        #print(turtle_color)
        tim.forward(50)
        x += 50
    x = -250
    y += 50


my_screen.exitonclick()
