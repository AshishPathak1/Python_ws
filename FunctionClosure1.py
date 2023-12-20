# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 23:02:49 2018

@author: Hrishikesh Pisal
"""

## Closure / Function Factory

def multiply_by(factor:int):
    """Return a function that multiplies values by the given factor"""
   #Local functions can access the state of surrounding environment
    def multiply(value:int)->int:
        """Multiply the given value by the factor already provided"""
        return value * factor # return value of multiply
    
    # enclosing function (multiply_by) returns nested function(multiply)
    return multiply 

if __name__ == '__main__':
    # multiply(4)
    times2 = multiply_by(2)
    print(times2)
    print(times2.__name__)
    print(times2.__doc__)
    print(id(times2))
    result = times2(10)
    print(result)
    
    times3 = multiply_by(3)
    print(times3)
    print(times3.__name__)
    print(times3.__doc__)
    print(id(times3))
    result = times3(10)
    print(result)
    
    
    print(times2(5))
    print(times3(5))
    
    mymulti = multiply_by
    del multiply_by
    
    print(times2(10))
    print(times3(10))  
    
    times5 = mymulti(5)
    print(times5(10))  