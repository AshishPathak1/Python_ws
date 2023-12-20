# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:29:24 2020

@author: Hrishikesh Pisal
"""


import functools
import time

def check_execution_time(func):
    """Print the runtime of the decorated function
    '''Moniters performace and gives result'''
    """
    
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        '''returns a float value of time in seconds.'''
        start_time = time.perf_counter()   
        
        value = func(*args, **kwargs)
        
        end_time = time.perf_counter()      
        run_time = end_time - start_time    
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return value
    
    return wrapper_timer

#end of decorator definition


# list_operation = check_execution_time(list_operation)

@check_execution_time
def list_operation(num_times):
    '''Returns the sum of squares of all numbers in the range(1,100001)
    repeated numtimes'''
    result = 0
    for element in range(1,(num_times+1)):
        result += sum([i**2 for i in range(1,100001)])
    return result
        

if __name__ == '__main__':
    list_operation(10)
    print(list_operation.__name__)
    print(list_operation.__doc__)