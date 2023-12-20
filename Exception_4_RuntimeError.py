# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 12:44:04 2018

@author: Hrishikesh Pisal
"""

def factorial(n:int)->int:
    if (not isinstance(n, int)):
        raise TypeError("The input should be of integer type")
    if (n < 0 ):
        raise ValueError("Cannot find Fctorial of -ve Integers")
    facto = 1
    for i in range(2,n+1):
        facto *= i
    return facto

def factorial_lib(n:int)->int:
    import math
    return math.factorial(n)


if __name__ == '__main__':
    try:
        # print(f"Factorial of seven is: {factorial('seven')}")
        # print(f"Factorial of -4 is: {factorial(-4)}")
        # print(f"Factorial of 12 is : {factorial(12)}")

        # print(f"Factorial of seven is: {factorial_lib('seven')}")
        # print(f"Factorial of -4 is: {factorial_lib(-4)}")
        print(f"Factorial of 12 is : {factorial_lib(12)}")        
        
    except TypeError as re:
        print(f"Error1 : {re}")
    except ValueError as e:
        print(f"Error2 : {e}")