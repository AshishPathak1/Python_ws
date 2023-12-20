# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 09:54:48 2018

@author: Hrishikesh Pisal
"""

# iterator with sentinal

print( "using range function")
for counter in range(1,6):
    print(counter)

print("using range object")
myRange = range(1,6)
for counter in myRange:
    print(counter)
    
sentinal = 7
# Error : Since range() is iterable and not callable
myIterator = iter(range(1,10),sentinal)

while(True):
    print(next(myIterator))

