# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:30:52 2018

@author: Hrishikesh Pisal
"""

# Nesting of Function Decorator 
# Returning Values From Decorated Functions

from FunctionDecorator4 import do_twice, debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


@do_twice
@debug
def greet(name):
    print(f"Hello {name}")
    return f"Hello {name}"    
    

# greet = do_twice(debug(greet))

if __name__ == '__main__':
    make_greeting("Lucky",age=21)
    greet("Shubra")
    print(greet("Fareed"))
    
    