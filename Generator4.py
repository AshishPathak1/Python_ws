# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:33:28 2018

@author: Hrishikesh Pisal
"""
# A return statement inside of a generator is equivalent to raise StopIteration() 


## Generator without raise StopIteration
def gen1():
    yield 99
    
    
## Generator using raise StopIteration
def gen2():
    yield 99
    raise StopIteration(-11)

## Generator using return
def gen3():
    yield 88
    return(-22)
    
if __name__ == '__main__':
    # generator = gen1()
    # print(next(generator))
    # print(next(generator))
    
    # generator = gen2()
    # print(next(generator))
    # print(next(generator))

    generator = gen3()
    print(next(generator))
    print(next(generator))
