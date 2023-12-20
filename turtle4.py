# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:00:15 2021

@author: Hrishikesh Pisal
"""
# Drawing Preset Figures

import turtle
import time

# Change the Screen Title
turtle.title("My Turtle Program")
# time.sleep(5)

# Return the TurtleScreen object the turtle is drawing on. 
# TurtleScreen methods can then be called for that object.
screen = turtle.getscreen()

# Kind of RawTurtle, has the same interface but draws on a default Screen 
my_turtle = turtle.Turtle()
your_turtle = turtle.Turtle()
# Set the turtle’s speed to an integer value in the range 0..10. 
# If no argument is given, return current speed.
my_turtle.speed("fast")

# turtle.circle(radius, extent=None, steps=None)
# Draw a circle with given radius. 
# my_turtle.circle(60)
# your_turtle.circle(100)

# time.sleep(2)
# Delete the turtle's drawings from the screen.
# my_turtle.clear()
# time.sleep(2)
# your_turtle.clear()

# Delete all drawings and all turtles from the TurtleScreen.
# turtle.clearscreen()
# Reset all Turtles on the Screen to their initial state.
# my_turtle.goto(20,500)
# your_turtle.goto(200,-200)
# turtle.resetscreen()


# my_turtle.circle(120, 90)  # draw a arc one  quater
# time.sleep(3)
# Delete the turtle’s drawings from the screen,
# re-center the turtle and set variables to the default values.
# my_turtle.reset()

# my_turtle.circle(120, 180)  # draw a semicircle
# time.sleep(3)
# my_turtle.reset()

# my_turtle.circle(120, 270)  # draw a three quater circle
# time.sleep(3)
# my_turtle.reset()

# my_turtle.circle(120, 360)  # draw a circle
# time.sleep(3)
# my_turtle.reset()
# time.sleep(2)

my_turtle.dot(20)
# time.sleep(2)
# my_turtle.circle(100)
time.sleep(2)
screen.bgcolor("violet")
my_turtle.circle(120)  # draws anticlockwise
my_turtle.circle(-120) # draws clock wise
# steps determines the number of steps to use.
# May be used to draw regular polygons.
# direction of the turtle is changed by the amount of extent.
my_turtle.circle(-150, 360, 5)
time.sleep(5)