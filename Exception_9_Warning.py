# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:29:46 2019

@author: Hrishikesh Pisal
"""

import warnings
import time

def adder(limit):
       
    if limit > 1000:
        warnings.simplefilter("ignore") ##ignore/default/error
        warnings.warn('Long Wait for result...')
    
    total=0
    for counter in range(1,limit+1):
        total = total + counter
        time.sleep(0.01)
    return total


def getElementFromCollection(coll,position)->int:
    warnings.simplefilter("default")
    # better verify if I can access coll[position] first
    if position > len(coll) or position <= 0:
        warnings.warn("Accesing element beyond the bounds.", RuntimeWarning)
        return -1
        
    return coll[position-1]
    

# python3 -W "ignore:do not:UserWarning::0" Exception_9_Warning.py
  
# the default behavior is to continue past that point and run the rest 
# of the program  
#Case1
# warnings.simplefilter("once")

# def function_with_warning():
#     warnings.warn('This is a warning!')
  
#Case2
def function_with_warning():
    # warnings.simplefilter("default")
    warnings.warn('This is a warning!')
    warnings.warn('This is a warning!')


def function_with_repeated_warning():
    warnings.simplefilter("once")
    warnings.warn('This is a warning!')
    warnings.warn('This is a warning!')
    warnings.warn('This is a warning!')
    warnings.warn('This is another warning!')
    warnings.warn('This is another warning!')
    warnings.warn('This is a warning!')
    print("Executing the function!")


def catch_warning_demo():
    warnings.filterwarnings('error', '.*very*')
    warnings.filterwarnings('error', '.*serious*')
    try:
        warnings.warn('This is a simple warning!')
        print("continuing after simple warning!")
        warnings.warn('This is a serious warning!')
        print("continuing after serious warning!")
    except Warning as werr:
        print(f"In except block {werr}")
 
def  catch_specific_warning_demo():
    warnings.filterwarnings('error', '.*very*')
    warnings.filterwarnings('error', '.*serious*')
    try:
        warnings.warn('This is a simple warning!',category=UserWarning)
        print("continuing after simple warning!")
        warnings.warn('This is a serious warning!',category=RuntimeWarning)
        print("continuing after serious warning!")
    except UserWarning as u_warn:
        print(f"Userwarning : {u_warn}")
    except RuntimeWarning as r_warn:
            print(f"RuntimeWarning : {r_warn}")

if __name__ == '__main__':
    print("Begining!")
    # print("Adding : ", adder(1001))
    # data = [10,20,30,40,50,60]
    # print("The Value is : ",getElementFromCollection(data,-5))
    # warnings.simplefilter("default")
    # function_with_warning()
    # function_with_warning()
    # function_with_warning()
    # function_with_warning()
    # function_with_repeated_warning()
    
    
    # catch_warning_demo()
    catch_specific_warning_demo()
    print("The End!")