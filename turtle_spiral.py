import turtle
import time
# factor = 10
my_turtle = turtle.Turtle()
x_cord = 0
y_cord = 0
# colours = ["white","black","red","green","blue","cyan","magenta","yellow","orange","purple","brown","pink","gray","lightgray","darkgray"]
for i in range (5,1300,5) :
    # my_turtle.color(colours[i])
    my_turtle.speed('fastest')
    my_turtle.circle(i,360, 4)
    # time.sleep(3)
    my_turtle.penup()
    my_turtle.goto(x_cord,y_cord)
    my_turtle.right(5.0)
    x_cord -=3
    y_cord -=3
    my_turtle.pendown()
turtle.done()