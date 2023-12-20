# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:52:14 2019

@author: Hrishikesh Pisal
"""
# Tail Recursive
# A tail recursive function is efficient for reducing stack size.

# Return the factorial for a specified number
def factorial(n):
    return factorialHelper(n, 1) # Call auxiliary function

# Auxiliary tail-recursive function for factorial
def factorialHelper(n, result):
    if n == 0:
        return result
    else:
        return factorialHelper(n - 1, n * result)

if __name__ == '__main__':
    print("Factorial of 5 = ",factorial(5))
    print("Time taken by Recursive Version")
   