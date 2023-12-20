# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:08:00 2018

@author: Hrishikesh Pisal
"""

def genSquares(limit:int):
    for i in range(1,(limit+1)):
        yield i ** 2 # Resume here later
    return

def genSquaresInf():
    counter = 0
    while True: #infinite loop
        counter = counter + 1
        yield counter ** 2 # Resume here later   
        
if __name__ == '__main__':
   # Get the Generator object
    sqrs = genSquares(5)
    print(next(sqrs))
    print(next(sqrs))
    print(next(sqrs))
    print(next(sqrs)) 
    
    #Generator objects are iterable
    sqrs = genSquares(5)
    for i in sqrs: # Resume the function
        print(i, end=' : ') # Print last yielded value
    print("\n")
    
    sqrs = genSquaresInf()
    print(next(sqrs))
    
    for i in sqrs: # Resume the function
        print(i, end=' : ') # Print last yielded value
    print("\n")
    print(next(sqrs))
   