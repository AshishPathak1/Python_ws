# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:32:39 2018

@author: Hrishikesh Pisal
"""
#A Tkinter widget can be bound to a function, 
#which is called when an event occurs.

import tkinter as tk
# from tkinter import Tk
# from tkinter import Button

# The program defines the functions processOK and processCancel 
# These functions are bound to the buttons when the buttons are 
# constructed. These functions are known as callback functions, 
# or handlers

def processOK():
    print("OK button is clicked")
 
def processCancel():
    print("Cancel button is clicked")


root = tk.Tk()  # Create a root window

# By default, fg is black and bg is gray for all widgets.

# binds the OK button to the processOK function,
btOK = tk.Button(root, 
              text   = "OK", 
              fg     = "red", 
              bg     = "green" ,
              padx   = 25,
              pady   = 10,
              command= processOK) # Callback / Handler

#binds the Cancel button to the processCancel function,
btCancel = tk.Button(root, 
                  text    = "Cancel", 
                  bg      = "yellow",
                  padx    = 15,
                  pady    = 10, 
                  command = processCancel)   # Callback / Handler

btOK.pack() # Place the button in the window
btCancel.pack() # Place the button in the window

root.mainloop() # Create an event loop

