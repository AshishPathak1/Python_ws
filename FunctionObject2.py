# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 23:32:09 2018

@author: Hrishikesh Pisal
"""

# Function as Objects : 
#       Functions Can Be Stored In Data Structures


# Name echo assigned to function object
def show(message): 
    print(message)

#embeds the function twice in a list of tuples, as
#a sort of actions table
schedule = [ (show, 'नमस्कार!'), (show, 'राम राम!') ]

func,arg = schedule[1]  #unpacking tuple
print(func.__name__, arg)

for (func, arg) in schedule:
    func(arg) # Call functions embedded in containers

#calling a function object stored in the 
#list without assigning it to a variable first. 
funcs = [str.lower, str.capitalize, str.upper]
print(funcs[1]('JAY HIND'))

schedule = [ (show, 'नमस्कार!'), (show, 'राम राम!') ]
schedule[1][0](schedule[1][1])
