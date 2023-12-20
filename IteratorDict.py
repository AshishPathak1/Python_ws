    # -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:11:04 2018

Iterator on Dictionary

@author: Hrishikesh Pisal
"""

statesCapital = {
    "Maharashtra"   : "Mumbai",      
    "Gujarat"       :"Gandhinagar",
    "TamilNadu"     :"Chennai",
    "Karnataka"     :"Banglore",
    "Kerala"        :"Thiruanantpuram",
    "Odisha"        :"Bhuvneshwar"
    }

for state in statesCapital:
    print(f"The capital of {state}, is {statesCapital.get(state)}")

# We can simulate this iteration behavior of the for loop in a while loop:
# the iteration runs over the keys of the dictionary

stateIterator = iter(statesCapital) # dict_keyiterator
print(f"State Iterator : {type(stateIterator)}")

while True:
    try:
        state = next(stateIterator)
        print(f'{state} : {statesCapital.get(state)}')
    except StopIteration:
        break
    
print("Bye Bye")