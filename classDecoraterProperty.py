# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:53:38 2019

@author: Hrishikesh Pisal
"""

class Person:
    '''This class represents a real world Person'''
    
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self): # name = property(name)
        '''This property represents Person's name'''
        print('fetch...')
        return self.__name
    
    @name.setter
    def name(self, value): # name = name.setter(value)
        print('change...')
        self.__name = value
        
    @name.deleter
    def name(self): # name = name.deleter(name)
        print('remove...')
        del self.__name
        
if __name__ == '__main__':        
    p1 = Person('Bobby Deol') # bobby has a managed attribute
    print(p1.name) # Runs name getter
    
#    When run, the decorated method is automatically 
#    passed to the first argument of the property built-in.
#    name = property(name)
   
    p1.name = 'Sunny Deol' # Runs name setter 
    print(p1.name)
   
    del p1.name # Runs name deleter 
    # print(p1.name)
    
    print('-'*20)
    p2 = Person('Jonny') # Jonny inherits property too
    print(p2.name)
    p2.name = "Jonny Lever"
    print(p2.name)
#    
    print(Person.__doc__)
    print(Person.name.__doc__) # Or help(Person.name)
