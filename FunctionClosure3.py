# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 07:38:45 2018

@author: Hrishikesh Pisal
"""
glb_var = "Hi!, i'am global"
state   = "Hi I am global state"

# Closure : Non Local
 
def tester(start):
    state = start # Each call gets its own state
    state = state + 1
    
    def nested(label):
        # Nonlocals must already exist in enclosing def!
        nonlocal state # Remembers state in enclosing scope
        print(f"{label}, {state}, {start}, {glb_var}")
        # Allowed to change it if nonlocal
        state =  state + 1
    
    return nested

if __name__ == '__main__':
    getting = tester(5)
    getting("First")
    getting("Second")
    getting("Third")
      
    # setting = tester(10)
    # setting("One")
    
    
    print(getting.__closure__)
    print(type(getting.__closure__))  #tuple
    print(type(getting.__closure__[0])) #tuple::cell
    print(type(getting.__closure__[0].cell_contents)) #tuple::cell::int
    
    print(getting.__closure__[0].cell_contents)  #start
    print(getting.__closure__[1].cell_contents)  #state
    
    # Number of variables of the sorrounding scope that the nested function is accessing
    print(f"Number of variables: {len(getting.__closure__)} ")
    
    getting("Hello")
    print(getting.__closure__[0].cell_contents)
    print(getting.__closure__[1].cell_contents)
    
    getting("Hi")
    print(getting.__closure__[0].cell_contents)
    print(getting.__closure__[1].cell_contents)
