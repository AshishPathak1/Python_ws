# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:26:52 2018

@author: Hrishikesh Pisal
"""
import tkinter as tk  
#The place manager places widgets in absolute positions
#The place manager is not compatible with all computers
#you should generally avoid using the place manager
  
class PlaceManagerDemo:
    def __init__(self):
        window = tk.Tk() # Create a window
        window.title("Place Manager Demo") # Set title
        
        tk.Label(window, 
              text = "Blue",    
              fg   = 'white', 
              bg="blue").place(x = 20, y = 20)
        
        tk.Label(window, 
              text = "Red",     
              fg   = 'white', 
              bg   = "red").place(x = 150, y = 50)
        
        tk.Label(window, 
              text = "Green",   
              fg   = 'white', 
              bg   = "green").place(x = 80, y = 80)
        
        window.mainloop() # Create an event loop

PlaceManagerDemo() # Create GUI 