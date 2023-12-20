# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:19:22 2018

@author: Hrishikesh Pisal
"""
import tkinter as tk

# The pack manager can place widgets on top of each other or
# place them side by side. You can also use the fill option to
# make a widget fill its entire container.


class PackManagerDemo:
    
    def __init__(self):
        window = tk.Tk()  # Create a window
        window.title("Pack Manager Demo 1")  # Set title
        window.geometry("200x100+700+100") # 200x100: dimension; 700+500:Position
        # lbl = tk.Label(window, 
        #                 text = "Blue",
        #                 bg   = "blue",
        #                 fg   = "white")
        
        # lbl.pack(side = tk.RIGHT)

# The fill option uses named constants X, Y, or BOTH to fill horizontally, 
# vertically, or both ways. The expand option tells the pack manager to 
# assign additional space to the widget. 

# If the parent widget is larger than necessary to hold all the 
# packed widgets, any extra space is distributed among the widgets 
# whose expand option is set to a nonzero value
        
        # tk.Label(window, 
        #           text = "Red",
        #           fg   = 'white', 
        #           bg   = "red").pack(fill = tk.X, expand = 1, side = tk.LEFT)
        
        # tk.Label(window, 
        #       text = "Green",
        #       fg   = 'white', 
        #       bg   = "green").pack(fill = tk.Y, expand=0,side= tk.LEFT)
        
        tk.Label(window,
                  text = "Cyan",
                  fg   = 'black',
                  bg   = "cyan").pack(fill = tk.X, expand=1, side = tk.RIGHT)
     
        
        # tk.Label(window, 
        #       text = "Yellow",
        #       fg   = 'black', 
        #       bg   = "yellow").pack(fill = tk.Y, expand=0, side=tk.LEFT)
        
       
        
#       The side option can be LEFT, RIGHT, TOP, or BOTTOM.
#       By default, it is set to TOP   

        tk.Label(window,
                  text = "Blue",
                  fg   = 'white',
                  bg   = "blue").pack(fill = tk.X, side = tk.LEFT,expand=0)
        
        
        # tk.Label(window,
        #           text = "Red",
        #           bg   = "red").pack(fill = tk.BOTH, expand = 1)
        
        # tk.Label(window, 
        #       text = "Pink", 
        #       bg   = "pink").pack(fill = tk.X, expand = 1, side = tk.LEFT)
        
        window.mainloop() # Create an event loop

if __name__ == '__main__':
    PackManagerDemo() # Create GUI 