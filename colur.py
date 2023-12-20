import turtle
import time

# Change the Screen Title
turtle.title("My Turtle Program")

my_turtle = turtle.Turtle()

colors = ["lime","yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black"]

my_turtle.speed("fastest")
my_turtle.pensize(5)
# Makes the turtle invisible.
my_turtle.hideturtle()

start_point_y = 0
radius = 10

while radius <= 250:
    my_turtle.up()  # penup()
    start_point_y -= 15  # a -= b : a = a -b
    #reset the y-cord for the turtle
    my_turtle.sety(start_point_y)
    my_turtle.down()
    my_turtle.pencolor(colors[radius%len(colors)])
    my_turtle.circle(radius)
    radius = radius + 15
time.sleep(3)
start_point_y = start_point_y - 15
radius = radius - 15
while radius >= 0:
    my_turtle.up()  # penup()
    start_point_y +=15   # a -= b : a = a -b
    #reset the y-cord for the turtle
    my_turtle.sety(start_point_y)
    my_turtle.down()
    my_turtle.pencolor("white")
    my_turtle.circle(radius)
    radius = radius - 15
time.sleep(5)

my_turtle.bye()