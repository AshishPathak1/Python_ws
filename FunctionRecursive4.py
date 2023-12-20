# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:54:29 2022

@author: Hrishikesh Pisal
"""
import time
import sys

sys.setrecursionlimit(500)

def countdown(number:int)->None:
    while(number > 0 ):
        print(f"{number}...")
        # time.sleep(0.01)
        number = number - 1
    print("blast off!!")
    return

def countdown_rec(number:int)->None:
    if(number > 0 ):
        print(f"{number}...")
        # time.sleep(0.01)
        countdown_rec(number-1)
    return
    
if __name__ == '__main__':
    # countdown(1000)
    countdown_rec(1000)