# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:31:31 2023

@author: hrish
"""

class RationalNumber:
    def __is_denominator_valid(denominator):
        if not isinstance(denominator, (int,float)):
            raise TypeError("Denominator has to be numeric")
        if denominator == 0:
            raise ValueError("Denominator should be Non-Zero numeric value")
            
    def __init__(self,numerator=0,denominator=1):
        RationalNumber.__is_denominator_valid(denominator)

        self.__numerator = numerator
        self.__denominator = denominator
        
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __add__(self,rn):
        temp = RationalNumber()
        if self.__denominator == rn.__denominator:
            temp.__denominator = self.__denominator
            temp.__numerator = self.__numerator + rn.__numerator
            return temp
        else:
            temp.__numerator = ((self.__numerator * rn.__denominator) + (rn.__numerator * self.__denominator))
            temp.__denominator = (self.__denominator * rn.__denominator)
            return temp
        
    def __sub__(self,rn):
        temp = RationalNumber()
        if self.__denominator == rn.__denominator:
            temp.__denominator = self.__denominator
            temp.__numerator = self.__numerator - rn.__numerator
            return temp
        else:
            temp.__numerator = ((rn.__numerator * self.__denominator) - (self.__numerator * rn.__denominator) )
            temp.__denominator = (self.__denominator * rn.__denominator)
            return temp
        
    def __mul__(self,rn):
        temp = RationalNumber()
        temp.__denominator = self.__denominator * rn.__denominator
        temp.__numerator = self.__numerator * rn.__numerator
        return temp
    
    def __le__(self,rn):
        if self.__denominator == rn.__denominator:
            return self.__numerator <= rn.__numerator
        else:
            self.__numerator = self.__numerator * rn.__denominator
            rn.__numerator = rn.__numerator * self.__denominator
            return self.__numerator <= rn.__numerator
        
    def __eq__(self,rn):
        if self.__denominator == rn.__denominator:
            return self.__numerator == rn.__numerator
        else:
            self.__numerator = self.__numerator * rn.__denominator
            rn.__numerator = rn.__numerator * self.__denominator
            return self.__numerator == rn.__numerator
        
    def __ne__(self,rn):
        if self.__denominator == rn.__denominator:
            return self.__numerator != rn.__numerator
        else:
            self.__numerator = self.__numerator * rn.__denominator
            rn.__numerator = rn.__numerator * self.__denominator
            return self.__numerator != rn.__numerator
        
    def __ge__(self,rn):
        if self.__denominator == rn.__denominator:
            return self.__numerator >= rn.__numerator
        else:
            self.__numerator = self.__numerator * rn.__denominator
            rn.__numerator = rn.__numerator * self.__denominator
            return self.__numerator >= rn.__numerator

    def __gt__(self,rn):
        if self.__denominator == rn.__denominator:
            return self.__numerator > rn.__numerator
        else:
            self.__numerator = self.__numerator * rn.__denominator
            rn.__numerator = rn.__numerator * self.__denominator
            return self.__numerator > rn.__numerator
        
    def __repr__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __pos__(self):
        return f"{self.__numerator:+}/{self.__denominator}"
    
if __name__ == '__main__':
    r1 = RationalNumber(3,5)
    r2 = RationalNumber(2,6)
    r3 = r2 + r1
    print(r3)
    r3 = r2 - r1
    print(r3)
    r3 = r2 * r1
    r3 = r2 > r1
    print(r3)   
    r3 = r2 < r1
    print(r3)   
    r3 = r2 <= r1
    print(r3)   
    r3 = r2 == r1
    print(r3)   
    r3 = r2 != r1
    print(r3)   
    r3 = r2 >= r1
    print(r3)      