# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:20:55 2018

@author: Hrishikesh Pisal
"""

## It’s much better to use a class to keep track of all
## individual widgets which may need to reference each other.

import tkinter as tk

# Root class inheriting from Tkinter’s Tk
# This creates a toplevel widget of Tk which usually is the main window of 
# an application. 


class SimpleUI(tk.Tk):  
    
    def __init__(self):
        super().__init__()
        
        self.iconbitmap('image/pen.ico')
        # The padx and pady arguments add padding horizontally & vertically.
        self.__label  = tk.Label(self, 
                                 text ="Hello World", 
                                 padx = 5,      pady = 5,
                                 fg   = "red",  bg   = "yellow")        
        
        # Create a button
        self.__button = tk.Button(self, 
                                  text = "Click Me",
                                  fg = "blue", bg = "white") 
        
        self.__label.pack()  # Display the label in the window
        self.__button.pack() # Display the button in the window

if __name__ == "__main__":
    root = SimpleUI()
        
    root.mainloop()
    
    