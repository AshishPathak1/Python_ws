# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:10:44 2018

@author: Hrishikesh Pisal
"""
import functools

def repeat(num_times):
    '''I am repeator'''
    
    def decorator_repeat(func):
        '''I am decorator'''
        functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            '''I am wrapper'''
            # nonlocal num_times
            for t in range(2):
                value = func(*args, **kwargs)
            # print(value)
            return value
        
        return wrapper_repeat
    
    return decorator_repeat


@repeat(num_times=10)
def greet(name):
    '''I am greeting'''
    print(f"Hello! {name}")
    
greet = repeat(3)(greet)
# greet = decorator_repeat(greet)
# greet = wrapper_repeat

    
if __name__ =='__main__':
    greet("Amar")
    