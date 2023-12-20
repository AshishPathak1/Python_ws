# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 12:12:34 2018

@author: Hrishikesh Pisal
"""

def simpleGen():
    counter = 1
    while True:
        data = yield counter
        print("data sent :", data)
        counter = counter + 1
              
g = simpleGen()
print(next(g))
print(g.send("Hi"))
print(g.send("Bye"))
print(g.send("Yeah"))
