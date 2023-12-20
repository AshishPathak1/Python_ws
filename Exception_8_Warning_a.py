# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:41:45 2023

@author: hrish
"""
import warnings

def doit():
    print("Doing it")
    warnings.warn(message='This is a user message',category=UserWarning)
    warnings.warn(message='This is a user message',category=UserWarning)
    print("done")