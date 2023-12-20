# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:43:38 2021

@author: Hrishikesh Pisal
"""
import turtle
import time

# Change the Screen Title
turtle.title("My Turtle Program")

my_turtle = turtle.Turtle()

# Picking the Pen Up and Down
# my_turtle.pen(pencolor="purple", pensize=10)
# my_turtle.speed("slowest")
# my_turtle.fd(100)
# my_turtle.rt(90)

# Pull the pen up – no drawing when moving.
# my_turtle.penup()
# my_turtle.fd(100)
# my_turtle.rt(90)

# Pull the pen down – drawing when moving
# my_turtle.pendown()
# my_turtle.fd(100)
# my_turtle.rt(90)
# time.sleep(5)


# Resetting the Environment
# The screen will get cleared up, and the turtle’s settings will all be 
# restored to their default parameters
my_turtle.reset()

my_turtle.shapesize(10,10,5)
my_turtle.pen(pencolor="purple", pensize=5)
# Stamp a copy of the turtle shape onto the canvas at the current turtle position
# id1 = my_turtle.stamp()
# print(id1)
# time.sleep(2)
# my_turtle.fd(100)
# id2 = my_turtle.stamp()
# print(id2)
# my_turtle.fd(100)
# time.sleep(2)
# Delete stamp with given stampid.
# my_turtle.clearstamp(id1)
# time.sleep(2)
# my_turtle.fd(100)
# my_turtle.clearstamp(id2)
# time.sleep(2)

my_turtle.home()
my_turtle.stamp()
my_turtle.fd(100)

my_turtle.stamp()
my_turtle.fd(100)

my_turtle.stamp()
my_turtle.fd(100)

my_turtle.stamp()
my_turtle.fd(100)

my_turtle.stamp()
my_turtle.fd(100)

time.sleep(2)

# Delete all or first/last n of turtle’s stamps
# my_turtle.clearstamps(3)  # Delete the first 3 stamps
# my_turtle.clearstamps(-3)   # Delete the last 3 stamps
my_turtle.clearstamps()   # Delete all the stamps
time.sleep(5)