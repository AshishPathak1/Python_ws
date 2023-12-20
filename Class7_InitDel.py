# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:46:59 2018

@author: Hrishikesh Pisal
"""

# Class with _ _ init _ _ method for initialization
# class with _ _ del _ _ method for cleanup

class Person:
    '''Simple class describing a Person'''
    
    def __init__(self, name):  
        ''' Constructor function '''
        print(name + " is created")
        self.__name = name # field self.name is initialized 
                           # with parameter name
    
    def sayHi(self)->None:   
        '''Prints Say hi for the person'''
        print(f"{self.__name} says Hi!")

    def __del__(self)->None:         
        ''' Destructor function'''
        print(f'Person {self.__name} is destroyed')

    def __str__(self)->str:
        '''Returns String representation of the Object'''
        return f"Hi! I am {self.__name}"
    
    def __repr__(self)->str:
        '''Returns String representation of the object in the Shell'''
        return f"Hello!, I am {self.__name}"
    
# end of the class

def baz():
    p = Person("Sammy")
    p.sayHi()
    print(p)
    # on returning from this function the local object
    # goes out of scope and the __del__ is called for 
    # all those objects that go out of scope
    
if __name__ == '__main__':
    baz()
    
    # object is created
    p = Person('Raja')  # __init__ in invoked automatically
    p.sayHi() # method is called; Person.sayHi(p)
    print(p)   # __str__() in invoked automatically
    # calling del to destroy object 
    del p     # __del__() is automatically called
   
    p = Person('Rani')
    p.sayHi()    #  Person.sayHi(p)
    print(p)
    del p     # destroying object
    p.sayHi()
    
    baz()   #calling a function
  
    print("Back to main")





    # def __del__(self)->None:         
    #     ''' Destructor function'''
    #     print(f'Person {self.__name} is destroyed')

    # def __str__(self)->str:
    #     '''Returns String representation of the Object'''
    #     return f"Hi! I am {self.__name}"
    
    # def __repr__(self)->str:
    #     '''Returns String representation of the object in the Shell'''
    #     return f"Hello!, I am {self.__name}"