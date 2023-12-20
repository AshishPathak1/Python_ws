# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:42:24 2018

@author: Hrishikesh Pisal
"""
#Program that uses the widgets Frame, Button, Checkbutton, 
#Radiobutton, Label, Entry (also known as a text field), 
#Message, and Text (also known as a text area).

import tkinter as tk

  
class WidgetsDemo:
    
    def __init__(self):
        window = tk.Tk() # Create a window
        window.title("Widgets Demo") # Set a title
#       To set the size of the window, we have to make
#       use of the wm.geometry option.
        window.geometry("600x400")
        # window["bg"] = "green"
#       The Frame class is used to create a frame
        frame1 = tk.Frame(window) # Create a Frame with Window as Parent
        self.__composeFrame1(frame1)
        
        # Add a button, a check button, and a radio button to frame1
        frame2 = tk.Frame(window) # Create and add a frame to window
        self.__composeFrame2(frame2)
        
#       Formatted text display. Allows you to display and edit text with 
#       various styles and attributes. 
#       Also supports embedded images and windows.
        text = tk.Text(window) # Create a text add to the window
        self.__composeText(text)
        
        window.mainloop() # Create an event loop
        
 

    def __composeFrame1(self,frame1:tk.Frame):
        frame1.pack(side= "top")  # and add a frame to window (top/left/right)
        # frame1["bg"] = "cyan"
        
# We can query whether or not the box has been checked by
# attaching a tkinter variable to it (StringVar, IntVar etc) 
# with variable=self.my_variable. 
# By default the value of this variable will be 1 when checked and 0 when not. 
# We can change this with the onvalue and offvalue arguments. 
# Changing the linked variable directly will update the associated 
# Checkbutton automatically
        
        self.__v0 = tk.IntVar()
        # self.v0.set(44)
        # print(self.v0.get())
        cbtBold = tk.Checkbutton(frame1, 
                                 text     = "Bold", 
                                 variable = self.__v0, 
                                 command  = self.__processCheckbtnBold)
       
        self.__v1 = tk.IntVar()
        cbtPlain = tk.Checkbutton(frame1, 
                                  text = "Plain", 
                                  variable = self.__v1, 
                                  command = self.__processCheckbtnPlain)
       
        self.__v2 = tk.IntVar()
        rbRed = tk.Radiobutton(frame1, 
                               text     = "Red", 
                               bg       = "red",
                               variable = self.__v2, 
                               value    = 1, 
                               command  = self.__processRadiobutton) 
       
        rbYellow = tk.Radiobutton(frame1, 
                                text     = "Yellow", 
                                bg       = "yellow",  
                                variable = self.__v2,
                                value    = 2,
                                command  = self.__processRadiobutton) 
        
#       The grid geometry manager is used to place the check 
#       button and radio buttons into frame1.
        cbtPlain.grid(row = 1, column = 1)
        cbtBold.grid( row = 1, column = 2)
        rbRed.grid(   row = 2, column = 1)
        rbYellow.grid(row = 2, column = 2)
        
   
    def __composeFrame2(self,frame2:tk.Frame):
        # frame2["bg"] = "green"
        frame2.pack(side="top")
        label = tk.Label(frame2, 
                         text = "Enter your name: ")
        
        self.__name = tk.StringVar()
#       A text entry field, also called a text field or a text box.
        entryName = tk.Entry(frame2, 
                             textvariable = self.__name) 
        
#       A simple button, used to execute a command.        
        btGetName = tk.Button(frame2, 
                              text = "Get Name", 
                              command = self.__processGetNameBtn)
        
#       Displays a text. Similar to the label widget, 
#       but can automatically wrap text to a given width 
        message = tk.Message(frame2, 
                             text = "It is a e e e e e a widgets demo",
                             padx = 5,
                             width  = 100,
                             )
        message["bg"] = 'yellow'
    
        label.grid(    row = 1, column = 1, padx = 10, pady = 10)
        entryName.grid(row = 1, column = 2, padx = 10, pady = 10)
        btGetName.grid(row = 1, column = 3, padx = 10, pady = 10)
        message.grid(  row = 1, column = 4, padx = 10, pady = 10)
        
    def __composeText(self,text:tk.Text):
        text["bg"] = 'yellow'
        text.pack(side="top")
        text["wrap"] = "word"    # none / char / word
#       If index is specified as END then the new elements 
#       are added to the end
        text.insert(tk.END, 
            "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(tk.END, 
            "these carefully designed examples and use them ")
        text.insert(tk.END, "to create your applications.")
        
 
    def __processCheckbtnBold(self):
        print("Bold Button is :" 
            + ("checked " if self.__v0.get() == 1 else "unchecked"))
   
    def __processCheckbtnPlain(self):
        print("Plain Button is " 
            + ("checked " if self.__v1.get() == 1 else "unchecked"))
         
    def __processRadiobutton(self):
        print(("Red" if self.__v2.get() == 1 else "Yellow") 
            + " is selected " )
    
    def __processGetNameBtn(self):
        print("Your name is " + self.__name.get())


        
if __name__ == "__main__":
    myGui = WidgetsDemo() # Create GUI

