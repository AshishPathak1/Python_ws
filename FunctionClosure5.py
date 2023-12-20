# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:27:52 2019

@author: Hrishikesh Pisal
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 07:38:45 2018

@author: Hrishikesh Pisal
"""

# Closure : Non Local
# enclosing function returning more than one functions
# the nested functions share the same copy of the variables 
# from enclosing scope

def tester(start, end):
    state = start  # Each call gets its own state

    def nested1(label):
        # Nonlocals must already exist in enclosing def!
        nonlocal state # Remembers state in enclosing scope
        print(label, state, end)
        state += 1 # Allowed to change it if nonlocal
    
    def nested2():
        # return start
        return state
    
    return nested1, nested2

if __name__ == '__main__':
    result = tester(5,10)
    print(f"type : {type(result)}")
    print(f"content : \n{result[0]},\n{result[1]}")
    
    tt = tester(50,109)
    tt[0]("nested1 check") # calls nested1
    print(tt[1]())         # calls nested2 
    
    
    f1, f2 = tt
    print(f"first function returned by tester()  {f1.__name__}")
    print(f"second function returned by tester() {f2.__name__}")
    f1("Hello")
    print(f2())
    # even after the enclosing function is destroyed the
    # nested function remembers the state of the non-local variables
    del tester
    f1("Hello")
    print(f2())

