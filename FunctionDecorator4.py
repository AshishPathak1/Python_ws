# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 08:49:00 2018

@author: Hrishikesh Pisal
"""

# Reusable Decorators

def do_twice(func):
    '''decorator that calls function twice'''
    
    def wrapper_do_twice(*args, **kwargs):
        '''nested function inside decorator do_twice'''
        func(*args, **kwargs)
        return func(*args, **kwargs)
        
    return wrapper_do_twice
# end of decorator do_twice

def debug(func):
    """Print the function details """
    
    def wrapper_debug(*args, **kwargs):
        print(f"Calling {func.__name__!r} with {(len(args)+len(kwargs))!r} arguments")
        print("side effect :\n",end="")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           
        return value
    
    return wrapper_debug

#end of decorator debug

def foo(*arg,**kwargs):
    print(arg)
    print(kwargs)
    pass


@do_twice
def say_hello():
  '''Greets you '''
  print("hello")
  return "Bye"

say_hello = do_twice(say_hello)

say_hello = debug(do_twice(say_hello))

# say_hello = do_twice(debug(say_hello))

@debug
def greet(*args):
    for name in args:
        print(f"Hello {name}")
    return '*'

greet = debug(greet)

if __name__ =='__main__':
    say_hello()	
    print(say_hello())
    say_hello("Dheeraj","Manish") # Error
    greet("Dheeraj","Manish")	
    print(greet("Dheeraj","Manish")	)
