# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:30:52 2018

Generator Basics

@author: Hrishikesh Pisal
"""
def foo():
    print('Cricket')
    print('Kabaddi')
    print('Lingrochya')
    print('Hockey')
    return
  

def sportsGenerator():
    counter = 1
    print("getting sport : ", counter)
    counter = counter + 1
    yield("Cricket")
    print("getting sport : ", counter)
    counter = counter + 1
    yield("FootBall") 
    print("getting sport : ", counter)
    counter = counter + 1
    yield("Hockey")
    print("getting sport : ", counter)
    counter = counter + 1
    yield("Tennis")
    print("getting sport : ", counter)
    counter = counter + 1
    yield("BasketBall") 
    print("getting sport : ", counter)
    counter = counter + 1
    yield("Kabaddi")
    return 'No more sports'
   

if __name__ == '__main__':
    # foo()
    # foo()
    # foo()
     
    ## returns a  iterator, i.e. a generator object
    sport = sportsGenerator() 
    print(sport)
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    
    # ## The iterator can be used by calling the next method.
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    # print("Sport : ", sport.__next__())
    # print("Sport : ",next(sport)) ## StopIteration Exception
    
    
    # names = ["Leela","Seema","Gopi","Nandana"]
    # list_iter = iter(names)
    # print(f"Name : {next(list_iter)}")
    
    # for name in names:
    #     print(f"Name : {name}")
        
        
    # sport = sportsGenerator() 
    # for mysport in sport:
    #     print(f"Sport : {mysport}")
