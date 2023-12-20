# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 07:33:08 2018

@author: Hrishikesh Pisal
"""

# Functions Can Be Passed To Other Functions

def yell(text:str)->str:
    return f"{text.upper()}!! 🤬😡"

def greeting(name:str)->str:
    return f"Hello {name} Good Evening"

def call(func, text:str)->None:
    message = func(text) #indirect call
    print(message)
    
if __name__ == '__main__':
    
    #userdefined function as first parameter
    call(yell,"Puja")
    call(greeting,"Puja")  
    
    #predefined function as first parameter
    call(str.lower,"AKASH") 
    call(str.capitalize,"AKASH") 
