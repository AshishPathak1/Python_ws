# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:18:26 2018

@author: Hrishikesh Pisal
"""

## ValueError : 
# Raised when an operation or function receives an argument that 
# has the right type but an inappropriate value

# The else clause is meant to contain code that needs to be executed 
# if the try clause did not raise any exceptions. 


def getNumber(inputMsg):
    while True:
        try:
            numberString = input(inputMsg)
            number = eval(numberString)
        except ValueError:
            print("The input value has to be a number in decimal format!")
        except NameError:
            print("The input shoud be numeric and not a string")
        else:
            return number
    
def performDivision():
    try:
        dividend = getNumber("Please enter the dividend: ")
        divisor = getNumber("Please enter the divisor: ")
        print(f"\n{dividend:.2f} / {divisor:.2f} = {dividend/divisor:.2f}")
    except ZeroDivisionError:
        print("\nThe divisor should not be zero!")
        
if __name__ == '__main__':
    performDivision()