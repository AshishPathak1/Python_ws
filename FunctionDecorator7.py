# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:44:35 2020

@author: Hrishikesh Pisal
"""

from functools import wraps

def logged(func):
    '''Decorator logged that logs the function call'''
    @wraps(func)
    def with_logging(*args, **kwargs):
        '''Nested function inside decorator logged'''
        print(f"function {func.__name__} was called with arguments {args}")
        result = func(*args, **kwargs)
        return result
    
    return with_logging


@logged
def square(x):
   """returns the square of the argument passed"""
   return  x * x

square = logged(square)

@logged
def foo():
    print("I am in foo")

foo = logged(foo)

if __name__ == '__main__':
    friendList = list()
    square(10)

    # print(f.__name__)  # prints 'f'
    # print(f.__doc__)   # prints 'does some math'
    # foo()