# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 20:03:46 2022

@author: Hrishikesh Pisal
"""

# Dynamic Polymorphism
import abc

class Transport_vehicle(metaclass = abc.ABCMeta):
    def __init__(self, company, max_capacity):
        self.__company = company
        self.__max_cap = max_capacity
    
    @abc.abstractclassmethod
    def load_goods(self):
        pass
        # raise NotImplementedError("Implement method load_goods")
    
    @abc.abstractclassmethod
    def unload_goods(self):
        pass
        # raise NotImplementedError("Implement method load_goods")
          
    def __str__(self):
          return f"Name : {self.__company}\tMax Tonnage : {self.__max_cap}\n"
     

class CargoShip(Transport_vehicle):
    def __init__(self, company, max_capacity):
        super().__init__(company, max_capacity)
            
    def load_goods(self):
        print('Cargo ship has arrived')
        print("Loading goods using a crane\n")   
          
    def unload_goods(self):
        print("Unloading goods using a cranes")    
        print('Cargo Ship has left the port \n')
   
class CargoPlane(Transport_vehicle):
    def __init__(self, company, max_capacity):
       super().__init__(company, max_capacity)
    
    def load_goods(self):
        print('Cargo Plane has arrived')
        print("Loading goods using a fork_lift")   
             
    def unload_goods(self):
       print("Unloading goods using a fork_lift")
       print('Cargo Plane has taken off\n')
    
class GoodsTrain(Transport_vehicle):
    def __init__(self, company, max_capacity):
       super().__init__(company, max_capacity)
       
       
    def load_goods(self):
        print('Goods Train has arrived')
        print("Loading goods using a porter")   
             
    def unload_goods(self):
        print("Unloading goods using a porter")    
        print('Goods train has taken started\n')
    
    
def testclass():
    ship1 = CargoShip("USS_QUALA",300000)
    ship1.load_goods()
    ship1.unload_goods()
    print(ship1)
    
    plane1 = CargoPlane("FedEX",100000)
    plane1.load_goods()
    plane1.unload_goods()
    print(plane1)
    
    train1 = GoodsTrain("Tata", 40000000)
    train1.load_goods()
    train1.unload_goods()
    
    veh = Transport_vehicle("TVeh",5445545)
    print(veh)
    veh.load_goods()
    veh.unload_goods()

def getTransportVehicle()->Transport_vehicle:
    from typing import Final
    max_carring_weight_plane:Final[int] = 100000
    max_carring_weight_ship:Final[int]  = 500000
    max_carring_weight_train:Final[int] = 1000000
    
    weight = eval(input("How many ton weight do you wish to carry ?"))
    if weight <= max_carring_weight_plane:
        return CargoPlane("FedEx", weight)
    elif weight <= max_carring_weight_ship:
        return CargoShip("MissionMumbai", weight)
    elif weight <= max_carring_weight_train:
        return GoodsTrain("IR", weight)
    else:
        return "Sorry Vehicle not avaiable"
    
    
def transportGoods():
    vehicle = getTransportVehicle()
    if isinstance(vehicle, Transport_vehicle):
        vehicle.load_goods()
        vehicle.unload_goods()  
    else:
        print("Not having Apporpriate vehicle to carry goods")
    
    
if __name__ == '__main__':
    # testclass()
    transportGoods()
