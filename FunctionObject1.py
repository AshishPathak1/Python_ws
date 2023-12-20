# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 23:32:09 2018

@author: Hrishikesh Pisal
"""

# Function as Objects : 
#   Functions Can Be Stored In Data Structures
#   Attributes : __name__, __doc__, __defaults__

def multiply(n1=10, n2=5):
    '''x'''
    return n1*n2

def add(n1=1, n2=1):
    '''+'''
    return n1+n2

def divide(n1=1, n2=1):
    '''/'''
    return n1//n2

def power(n1=1, n2=1):
    '''**'''
    return n1**n2

#Set/List of User defined Functions{}/[]
user_defined_function_set = {add, multiply, divide, power}

# List of Methods(Function) : Predefined
predefined_defined_method_list = [str.lower, str.capitalize, str.upper]

predefined_defined_function_tuple = (len,sum,max,min)

if __name__ == '__main__':
    
    #Lists the str methods stored in list
    for func in predefined_defined_method_list:
        print(func)
    
    #Lists the predefiend functions stored in tuple
    for func in predefined_defined_function_tuple:
        print(f"\nname {func}) \nDescription : {func.__doc__}")
      
    #Lists the userdefined functions functions stored in set
    for func in user_defined_function_set:
        print(f"{func} at {id(func)} ")
        
        
    #Lists the str methods stored in list
    for func in predefined_defined_method_list:
        print(f"{func.__name__} is at {id(func)}")
    
    #Lists the predefiend functions stored in tuple
    for func in predefined_defined_function_tuple:
        print(func.__name__)
      
    #Lists the userdefined functions functions stored in set
    for func in user_defined_function_set:
        print(func.__name__)
        
    
    #Calls/Executes the functions stored in list
    for func in predefined_defined_method_list:
        print(f"{func.__name__:<15} : {func('HeY tHEre')}")

    n1 = 10
    n2 = 7
    
    # Sets are unodered by default
    for afunction in user_defined_function_set:
        print(f"{afunction.__name__:<15} : {afunction(n1,n2):<10}")

    for afunction in user_defined_function_set:
        print( f'{n1:<2} {afunction.__name__:^8} {n2:<2} = {afunction(n1,n2)}')
 
        
    for afunction in user_defined_function_set:
        res = f'{n1:<2} {afunction.__doc__:^2} {n2:<2} = {afunction(n1,n2)}'
        print(res)
        
    for afunction in user_defined_function_set:
        arg1, arg2 = afunction.__defaults__
        print( f'{arg1:4} {afunction.__doc__:^2} {arg2:2} = {afunction()}')
    