# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:33:55 2018

@author: Hrishikesh Pisal
"""

# Local Function / Nested function


def temperature(degCel:float)->float:
    '''
    Parameters
    ----------
    degCel : float
        Takes the temperature in Degree celcius as a single paramenter.

    Returns
    -------
    flaot
       Returns the temperature in Farenheit
    '''
   
    ## Local: Helper Function
    def celsius2fahrenheit(deg:float)->float: 
        return  deg * (9 / 5) + 32

    farenheit =  celsius2fahrenheit(degCel)
    return farenheit
 



if __name__ == '__main__':
    tempCel = float(input("Enter temperature in degree Celcius : "))
    tempFaren = temperature(tempCel)
    print(f"Temperature {tempCel}˚C in Farenheit is {tempFaren}˚F")
    
    # celsius2fahrenheit(tempCel) # error

