# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:47:11 2018

@author: Hrishikesh Pisal
"""

import tkinter as tk

# Create tk window
root_window = tk.Tk()

root_window.iconbitmap('image/pen.ico')
# tk.Label() which will hold our "Hello World" text. 
# The first argument to a Tk widget is the parent in which it will be placed.
label = tk.Label(root_window, 
                 text       = "Hello ! Welcome to Impetus", 
                 padx       = 50,  #internal padding x
                 pady       = 20,  #internal padding y
                 foreground = "black", 
                 background = "yellow")

# place the label into the root_window
label.pack()

# root_window.mainloop() is responsible for showing the window.
root_window.mainloop()