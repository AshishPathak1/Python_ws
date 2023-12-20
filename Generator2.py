# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:46:30 2018

Fibonacci Iterator

Since Python 3.3, generators can also use return statements,

@author: Hrishikesh Pisal
"""
# 0,1,1,2,3,5,8,13,21,34,...

def fibonacci_function(limit:int)->list:
    """ A function for creating finite series list of
    Fibonacci numbers """
    result = []
    a, b, c, counter = 0, 1, 0, 0
    
    while(counter != limit):
        result.append(c)
        a = b
        b = c
        c = a + b
        counter = counter + 1
    else:
        return  result 

#Better than previous
# def fibonacci_function(limit:int)->list:
    """ A function for creating finite series list of
    Fibonacci numbers """
    result = []
    a, b, counter = 0, 1, 0
    while(counter != limit):
        result.append(a)
        a, b = b, a + b
        counter = counter + 1
    else:
        return  result 




def fibonacciInf():
    """ A generator for creating infinite series of
    Fibonacci numbers """
    a, b, = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
        
       
def fibonacci(limit):
    """ A generator for creating finite series of
    Fibonacci numbers """
    a, b, counter = 0, 1, 1
    while counter <= limit:
        yield a
        a, b = b, a + b
        counter = counter + 1
    else:
        return "Yeah!" # since Python 3.3
               
    
    
if  __name__ == '__main__':     
    
    # LIMIT = 5
    # fibo_list = fibonacci_function(LIMIT)
    # print(f"first {LIMIT} numbers from fibonacci series are :")
    # for number in fibo_list:
    #     print(f"{number}, ",end="")
    # print()
    

    fibo_generator= fibonacciInf()
    value = next(fibo_generator)
    print(value)
    value = next(fibo_generator)
    print(value)
    value = next(fibo_generator)
    print(value)
    
    LIMIT = 5
    print("First",LIMIT,"Fibonacci numbers are :" )
    for value in range(LIMIT):
        print(next(fibo_generator)) # 
    print()
    
    
    fibo_generator= fibonacciInf()
    choice = 'y'
    while(choice.upper() in ['Y','YES']):
        print(next(fibo_generator))
        choice = input("Press 'y/yes' to continue or any other key to stop :")
        
    import time
    fibo_generator= fibonacciInf()
    for value in fibo_generator:
        print(value)
        time.sleep(2) 
        
        
    # LIMIT = 10
    # fibo_generator= fibonacci(LIMIT)
    # print(f"First {LIMIT} Fibonacci numbers are :" )
    # for value in fibo_generator:
    #     print(value) # 

    # LIMIT = 10
    # fibo_generator= fibonacci(LIMIT)
    # print(f"First {LIMIT} Fibonacci numbers are :" )
    # for value in range(LIMIT):
    #     print(next(fibo_generator)) # 
        
    # val = next(fibo_generator)
    # print(val)