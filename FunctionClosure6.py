# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:57:27 2020

@author: Hrishikesh Pisal
"""
# unlike the global statement, nonlocal names really must have previously 
# been assigned in an enclosing def’s scope when a nonlocal is evaluated,
# or else you’ll get an error
state = 10
def tester(start):
    
    def nested(label):
        nonlocal state # Nonlocals must already exist in enclosing def!
        state = 0
        print(label, state)
        
    return nested


def tester1(start):
    
    def nested(label):
        global state # Globals don't have to exist yet when declared
        state = 0 # This creates the name in the module now
        print(label, state)
        
    return nested

F = tester(0)
F('abc')
print(state)


# nonlocal restricts the scope lookup to just enclosing defs; nonlocals are not  looked up in the enclosing module’s global scope or the built-in scope outside all
# defs,
spam = 99
def tester():
    
    def nested():
        # nonlocal spam # Must be in a def, not the module!
        global spam
        print('Current=', spam)
        spam += 1

    return nested