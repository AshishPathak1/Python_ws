# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:44:39 2021

@author: Hrishikesh Pisal
"""

def getInteger()->int:
    integer = int(input("Please enter an Integer :"))
    return integer

def divide(numerator:int, denominator:int)->float:
    return numerator/ denominator

if __name__ == '__main__':
    numerator   = getInteger()
    denominator = getInteger()
    result      = divide(numerator, denominator)
    print(f"{numerator} / {denominator} = {result:<10.2f}")
