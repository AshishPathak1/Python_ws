# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:49:40 2018

@author: Hrishikesh Pisal
"""
# ABC and Polymorphism
import abc

class Vehicle(metaclass=abc.ABCMeta):
    def __init__(self, name): 
        if not Vehicle.__isNameValid(name):
            raise ValueError("Incorrect name!")
        self.__name = name
        
    @staticmethod
    def __isNameValid(name):
        if isinstance(name,str):
            if not name.isspace():
                return True
        return False
    
    def getName(self):
        return self.__name
    
    @abc.abstractmethod
    def drive(self):             
        pass
    
    @abc.abstractmethod
    def stop(self):             
        pass


class Sportscar(Vehicle):
    def __init__(self,name):
        super().__init__(name)
        
    def drive(self):
        return 'Driving Sportscar! Zoooommmm..'
 
    def stop(self):
        return 'Braking Sportscar!'
    def __str__(self):
        return f"Its a sportscar {self.getName()}"
 
class Truck(Vehicle):
    def __init__(self,name:str, max_wt:float):
        super().__init__(name)
        self.__max_wt = max_wt
   
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'
 
    def stop(self):
        return 'Braking Truck!'
    
    def __str__(self):
        return f"Its a {self.getName()} "
 
 
def use_Vehicle(v )->None:
    if isinstance(v,(Sportscar,Truck)):
        print(f"It's a {v.getName()}")
        print(v.drive())
        print(v.stop())
    else:
        print("Sorry! it's not a Vehicle")
    print()
    
    
class Pen:
    pass



if __name__ == '__main__':
    # Vehicle = Vehicle("XXX") # Abstract class cannot be instantiated
    Vehicle = Sportscar("XTreme")

    vehicle_list = [
        Truck('Banana truck',5),
        Truck('Orange truck',6),
        Sportscar('Porsche 911'),
        Pen()
                ]
    
    # for v in vehicle_list:
    #     print(v)
        
    for v in vehicle_list:
        use_Vehicle(v)