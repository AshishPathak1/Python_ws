# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:29:20 2018

@author: Hrishikesh Pisal
"""

# ArithmeticError : ZeroDivisionError

def divide(numerator, denominator):
    result =  numerator / denominator
    return result

     
def safeDivide(numerator:float, denominator:float)->float:
    try:
        result =  numerator / denominator
        
    except ZeroDivisionError:
        print('Denominator cannot be zero')
    except TypeError:
        print('Numerator and denominator should be of numeric type')
    except Exception: # handler for all other possible Exceptions
        print("Unknown error occured")
    else:
        # print(f"{numerator} / {denominator} = {result:<10.3f}")
        return result

if __name__ == '__main__':
    # print(divide(10,3))
    # print(divide(10,0))
    # print(divide('two'/'one'))
    # result =  safeDivide(20, 3.5)
    # result = safeDivide(20, 0)
    result = safeDivide('two','one')
    print (f"Result = {result}")
    print("The End!")