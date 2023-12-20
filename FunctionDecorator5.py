# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:02:12 2020

@author: Hrishikesh Pisal
"""


from FunctionDecorator4 import do_twice

@do_twice
def say_whee():
    print("Whee!")
    
    
    
if __name__ == '__main__':
    say_whee()
