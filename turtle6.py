# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:41:48 2021

@author: Hrishikesh Pisal
"""

import turtle
import time

screen = turtle.getscreen()
my_turtle = turtle.Turtle()

# Change the color of the turtle: This changes the fill color.
# Change the color of the pen: This changes the outline or the ink color.

# shapesize(wid;len,outline)
# my_turtle.shapesize(10,5,2)
# my_turtle.circle(120)
# time.sleep(2)
# my_turtle.shapesize(50,50,20)
# change the color of the turtle 
# my_turtle.fillcolor("red")
# my_turtle.circle(120)
# time.sleep(5)
# my_turtle.reset()

# my_turtle.shapesize(5,5,2)
# change the color of the pen (or the outline)
# my_turtle.pencolor("green")
# my_turtle.fillcolor("red")
# my_turtle.pensize(5)
# my_turtle.forward(400)
# time.sleep(3)

# my_turtle.reset()

# my_turtle.shapesize(10,10,5)
# To change the color of both
# fill = yellow
# outline = cyan
# my_turtle.color("blue", "red")
# my_turtle.pencolor("blue")
# my_turtle.pensize(5)
# my_turtle.forward(300)
# time.sleep(3)



my_turtle.reset()
my_turtle.speed("slowest")
my_turtle.pensize(5)
my_turtle.pencolor("green")
# Return or set the fillcolor.
my_turtle.fillcolor("red")
# my_turtle.fillcolor((50, 193, 143))
# my_turtle.fillcolor('#87aaa2')#'#7B43B0 ')
# my_turtle.fillcolor('#5228b7')
# Called just before drawing a shape to be filled.
# my_turtle.begin_fill()
# numberofturns = 0
# while (numberofturns <= 3):
#     my_turtle.forward(100)
#     my_turtle.left(90)
#     numberofturns = numberofturns + 1
# else:
# #     # Fill the shape drawn after the call begin_fill().
#     my_turtle.end_fill()
# time.sleep(3)


# color(colorstring1, colorstring2), color((r1,g1,b1), (r2,g2,b2))
# Equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
# my_turtle.speed("slowest")
# my_turtle.shapesize(3,3,3)
# my_turtle.color("cyan", "orange")
# my_turtle.backward(200)
# my_turtle.right(90)

# my_turtle.color("#f5d414", "#a0c8f0")
# my_turtle.backward(200)

# time.sleep(3)



# my_turtle.goto(200,200)
# my_turtle.home()
# my_turtle.clear()

# my_turtle.shapesize(30,30,3)
# # Changing the Turtle Shape
# my_turtle.shape("turtle")
# time.sleep(2)
# my_turtle.shape("arrow")
# time.sleep(2)
# my_turtle.shape("circle")
# time.sleep(2)
# my_turtle.shape("square")
# time.sleep(2)
# my_turtle.shape("triangle")
# time.sleep(2)
# my_turtle.shape("classic")
# time.sleep(2)


# Customizing in One Line
my_turtle.shapesize(5,5,3)
my_turtle.pen(pencolor="black", fillcolor="yellow", pensize=5, speed=1)
my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.shape("turtle")
my_turtle.circle(90)
my_turtle.end_fill()
time.sleep(5)

