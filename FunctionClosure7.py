# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:07:42 2020

@author: Hrishikesh Pisal
"""

# function attributes—user-defined names attached to
# functions directly.

def foo():
    ''' it's me fooo '''
    print("Inside foo")

foo.age = 8

print(foo.__name__)
print(foo.__doc__)
print(foo.age)


def tester(start):
    
    def nested(label):
        print(label, nested.state) # nested is in enclosing scope
        nested.state += 1 # Change attr, not nested itself
        
    nested.state = start # Initial state after func defined
    
    return nested
    
F = tester(0)
F('spam') # F is a 'nested' with state attached

F('ham')
print(F.state) # Can access state outside functions too


