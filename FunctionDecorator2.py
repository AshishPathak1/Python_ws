# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 08:49:00 2018

@author: Hrishikesh Pisal
"""

# Decorator without Argument

def capitalize(func):
    
    def uppercase():
        result = func()
        return result.upper()

    return uppercase


# @capitalize decorator takes in a callable(say_hello) 
# as an argument and returns another callable(uppercase).
@capitalize
def say_hello():
  return  "hello"

# old_sayHello = say_hello
# say_hello = capitalize(say_hello)

if __name__ =='__main__':
#    The decorator modifies the say_hello function by 
#    changing its result to uppercase.
    print(say_hello())	# 'HELLO'
