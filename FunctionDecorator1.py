# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:48:49 2018

@author: Hrishikesh Pisal
"""
# Simple Decorator : 
#       decorators wrap a function, modifying its behavior.

def my_decorator(func):
    ''' I am a decorator '''
    
    def wrapper():
        ''' I am a wrapper '''
        print("Before \"",func.__name__,"\" is called.")
        func()
        print("After \"", func.__name__,"\" is called.")
        
    return wrapper

def sayHello():
    ''' I am saying Hello '''
    print("Hello !")


# sayWhee = my_decorator(sayWhee)
@my_decorator
def sayWhee():
    ''' I am saying Whee '''
    print("Whee!")


if __name__ == '__main__':
    print(f"Function Name : {sayHello.__name__}")
    print(f"Function doc  : {sayHello.__doc__}")
    sayHello = my_decorator(sayHello)
    sayHello()
    print(f"Function Name : {sayHello.__name__}")
    print(f"Function doc  : {sayHello.__doc__}")
    
    ## Using Decorator
    sayWhee() 
    