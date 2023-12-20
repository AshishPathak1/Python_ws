# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 07:38:45 2018

@author: Hrishikesh Pisal
"""

# Closure : Non Local

val = 100  # Global variable

def closureFunc(up):
   print("Welcome to closureFunc") 
   val = 10   #local variable
   
   def nestedFunc():
       # global val
       nonlocal val
       print("Welcome To NestedFunct ")
       for i in range(1, up+1):
           val += i
       print(f"Total is =  {val}")
       
   print("Returning from closureFunc")     
   return nestedFunc

if __name__ == '__main__':
    getting = closureFunc(5)
    getting()
    
    
    del closureFunc
    another = closureFunc(10)
    another()
