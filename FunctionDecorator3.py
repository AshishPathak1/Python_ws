# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:03:07 2018

@author: Hrishikesh Pisal

function being decorated takes a parameter
"""
def capitalize(func):
    
    def uppercase(*args):
        result = func(*args)
        return result.upper()

    return uppercase


#decorating an function which takes in a parameter of type str
@capitalize
def say_hello(name:str):
  return f'hello!, {name}'

# say_hello = capitalize(say_hello)
# # say_hello = uppercase
# result = say_hello('Rutuja')
# print(result)


def validate(func):
    import sys
    def validate_function_parameter(*args):
        if not isinstance(args[0], int):
            print("Argument should be of type int")
            sys.exit(0)
        digit_sum  = func(args[0])
        return digit_sum
    
    return validate_function_parameter

@validate
def sum_of_digits(num:int)->int:
    digit_sum = 0
    while num != 0:
        digit_sum = digit_sum +  (num % 10)
        num = num // 10
    return digit_sum
  
      
# sum_of_digits = validate(sum_of_digits)
result = sum_of_digits(444)
print(result)   
result = sum_of_digits("444")
print(result)

@validate
def sum_of_factors(num:int)->int:
    factor_sum = 0
    for counter in range(1,(num//2)+1):
        if num % counter == 0:
            factor_sum += counter
    return factor_sum        
    


def squareit(func):
    
    def wrapper(*args):
        # print("Function actually called is :",wrapper.__name__)
        # print("Name of the function wrapped:",func.__name__)
        result = func(*args)
        return result ** 2
    
    return wrapper


@squareit
def get_reverse(data:int):
    return int(str(data)[::-1])  # returns the reverse

# get_reverse = squareit(get_reverse)

@squareit
def addition(*args):
    # print(type(args))
    # print(args)
    return sum(args[0])


#Decorating the predefined function
def mydeco(func):
    
    def myprint(*args):
        func('Started printing')
        for arg in args:
            func(f"**{arg}**")
        func('Finished printing')
    
    return myprint


   
if __name__ == '__main__':
    result = say_hello('mangesh')
    print(result)
    
    print(addition.__name__)
    print(addition([3,4]))
    print(addition(3,4,5))
    
    #passing predefined function to decorator
    print = mydeco(print)
    
    print("First")    # modified function is called
    print("First","Second","Third")
    del print
    print("Second")   # reverted to original behaviour
    print("first","Second","Third")