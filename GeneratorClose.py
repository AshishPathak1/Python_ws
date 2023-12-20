# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:05:44 2020

@author: Hrishikesh Pisal
"""

def greet(name:str)->str:
    while True:
        greetMsg = yield 
        yield greetMsg + " " + name

def genSquaresInf():
    i = 0
    while True:
        i = i + 1
        yield i ** 2 # Resume here later 
    
if __name__ == '__main__':
    # g = greet("Akash")
    # slangWordsList = ["OMG","TBH","Bruh","LMIRL"]
    # goodWordList = ["Good Morning","Good Evening","LMIRL","Good Afternoon","Good Night"]
    
    
    # for msg in slangWordsList:
    #     next(g)
    #     result = g.send(msg)
    #     print(result)
      
    # for msg in goodWordList:
    #     next(g)
    #     result = g.send(msg)
    #     print(result)
    
    # g = greet("Ashish")
    # for message in goodWordList:
    #     if message in slangWordsList:
    #         g.close()
    #         break
    #     next(g)
    #     result = g.send(message)
    #     print(result)
            
    
    # next(g)
        
    g = genSquaresInf()
    f = genSquaresInf()
    print(next(g))
    print(next(g))
    print(next(g))
    g.close()
    print(next(g))       
    g.send("x")
    print(next(f))
    f.close()
    print(next(f))
    
