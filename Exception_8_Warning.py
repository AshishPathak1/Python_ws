# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:29:46 2019

@author: Hrishikesh Pisal
"""
import warnings
 
def basic_warn1():
    print('Before the warning')
    print()
    warnings.warn('This is a warning message') #default - UserWarning
    # raise Exception("some Error!")
    print()
    print( 'After the warning')

def basic_warn2():
    # import math
    # n = 4.0
    # result = math.factorial(n)
    # print(f"Factorial of {n} = {result}")
  
    # try:
    #     n = 4.0
    #     # Call to factorial with floating point value 
    #     # results in DeprecationWarning warning
    #     result = math.factorial(n)
    #     print(f"Factorial of {n} = {result}")
    # except DeprecationWarning as err:
    #     print(f"Invalid type of input supplied!\n{err}")
        
    from collections import abc
    mydict = {'test_key': 'test_value'}
    result = isinstance(mydict, abc.Mapping)
            
def filter_demo():
    # warnings.filterwarnings('ignore', '.*do not.*',)
    warnings.filterwarnings('once', '.*do.*',)
    # warnings.filterwarnings('error', '.*do.*',)
    print('Before the warning')
    warnings.warn('Show this first warning message')
    warnings.warn('Just DO Not show this second message')
    warnings.warn('Just DO Not show this second message')
    warnings.warn('DO Not Show this third message')
    warnings.warn('Show this fourth warning message')
    warnings.warn('do Show this last fifth message')
    warnings.warn('This is the very last message')
    warnings.warn('This is the very last message')
    warnings.warn('Show this first warning message')
    
    print( 'After the warning')


# python -W "ignore:do not:UserWarning::0" demo.py
    
def warn_error():
    # This filter tells the warnings module to raise an exception when the 
    # warning is issued.
    # warnings.simplefilter(action='default', category=UserWarning,lineno=0)
    # warnings.simplefilter(action='ignore', category=UserWarning,lineno=0)
    # warnings.simplefilter(action='once', category=UserWarning,lineno=0)
    # warnings.simplefilter(action='ignore', category=UserWarning,lineno=66)
    # warnings.simplefilter(action='module', category=UserWarning)
    # warnings.simplefilter(action='default', category=RuntimeWarning)
    print('Before the warning')
    warnings.warn(message='This is a user message',category=UserWarning)
    warnings.warn(message='This is a user message',category=UserWarning)
    warnings.warn(message='This is a user message',category=UserWarning)
    
    warnings.warn(message='This is another user warning message',category=UserWarning)
    warnings.warn(message='This is a DW warning message',category=DeprecationWarning)
    warnings.warn(message='This is a user **** message') #default category is UserWarning
    warnings.warn(message='This is a RW warning message',category=RuntimeWarning)
    warnings.warn(message='This is a user message')  #default category is UserWarning
    warnings.warn(message='This is a user **** message')  #default category is UserWarning
    print( 'After the warning')
    
# to control from command prompt 
    
# python -W "error::UserWarning::0" warn_demo.py
# python -W "ignore::UserWarning::0" Exception_8_Warning.py

if __name__ == '__main__':
    warnings.simplefilter(action='module', category=UserWarning)
    import Exception_8_Warning_a
    Exception_8_Warning_a.doit()
    basic_warn1()
    # basic_warn2()
    # filter_demo()
    warn_error()
    print("That's all folks!")