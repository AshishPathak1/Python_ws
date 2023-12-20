# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:57:04 2021

@author: Hrishikesh Pisal
"""

# Drawing a Shape at different speed
import turtle
import time

screen = turtle.getscreen()
my_turtle = turtle.Turtle()

# Speeds from 1 to 10 enforce increasingly faster animation 
# of line drawing and turtle turning.
# an integer in the range 0..10 or a speedstring 

# my_turtle.speed(1)
# Speedstrings are mapped to speedvalues
# my_turtle.speed("slowest")

# my_turtle.speed(3)
# my_turtle.speed("slow")

# my_turtle.speed(6)
# my_turtle.speed("normal")

# my_turtle.speed(10)
# my_turtle.speed("fast")

# my_turtle.speed(0)
# my_turtle.speed("fastest")



my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(100)

time.sleep(2)