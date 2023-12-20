# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:37:21 2018

@author: Hrishikesh Pisal
"""
# Import tkinter
# Toplevel widget of Tk which represents mostly the main window
# of an application.
import tkinter as tk

#Using OOP
#There are two advantages of defining a class for creating a GUI 
#and processing GUI events. 
#First, you can reuse the class in the future. 
#Second, defining all the functions as methods enables them to 
#access instance data fields in the class.

class ProcessButtonEvent_UI(tk.Tk):
    
    def __init__(self):
        super().__init__() # Create a window
        
        self.__btOK     = tk.Button(self, 
                                 text    = "Okay", 
                                 fg      = "white",
                                 bg      = "#E015ED", 
                                 command = self.__processOK) 
        
        self.__btCancel = tk.Button(self, 
                                 text    = "Cancel", 
                                 bg      = "yellow", 
                                 command = self.__processCancel) 
        
        self.__btOK.pack() # Place the button in the window
        self.__btCancel.pack() # Place the button in the window

        self.mainloop() # Create an event loop

    def __processOK(self):
        print("OK button is clicked")
     
    def __processCancel(self):
        print("Cancel button is clicked")
# end of UI class



if __name__ == '__main__':        
    ProcessButtonEvent_UI() # Create an object to invoke __init__ method