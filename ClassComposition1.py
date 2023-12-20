# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:35:50 2018

@author: Hrishikesh Pisal
"""
## Aggregation

class Person(object):
    
    def __init__(self, name, yearOfBirth):
        self.__name = name
        self.__yearOfBirth = yearOfBirth
        
    def getName(self):
        return self.__name
    
    def getYearOfBirth(self):
        return self.__yearOfBirth
    
    def setName(self, newName):
        self.__name = newName
        
    def setYearOfBirth(self, yob):
        self.__yearOfBirth = yob
        
    def __str__(self):
        return f"Name : {self.__name}\nYear Of birth : {self.__yearOfBirth}"
    
    
class Doctor(object):
    
    def __init__(self, person:Person, specialization:str):
        self.__person = person
        self.__specialization = specialization

    def getSpecialization(self):
        return self.__specialization
    
    def setName(self,newName):
        self.__person.setName(newName)
      
    def setYearOfBirth(self, yob):
        self.__person.setYearOfBirth(yob)
        
    def getName(self):
        return self.__person.getName()
    
    def getYearOfBirth(self):
        return self.__person.getYearOfBirth()
    
    def __str__(self):
        return f"{self.__person}\nSpecialization : {self.__specialization}"



class Player:
    
    def __init__(self, person:Person, year:int):
        self.__person = person
        self.__debutYear = year

    def getDebutYear(self):
        return self.__debutYear
    
    def setName(self,newName):
        self.__person.setName(newName)
      
    def setYearOfBirth(self, yob):
        self.__person.setYearOfBirth(yob)
        
    def getName(self):
        return self.__person.getName()
    
    def getYearOfBirth(self):
        return self.__person.getYearOfBirth()
    
    def __str__(self):
        return f"{self.__person.__str__()}\nDebut Year : {self.__debutYear}"
           
def printAllDetails(*args):
    for data in args:
        # print(data.__str__())
        if isinstance(data, Person):
            print("\nPerson's Details :")
        elif isinstance(data, Doctor):
            print("\nDoctor's Details :")
        elif isinstance(data, Player):
            print("\nPlayer's Details :")
        
        print(data)
       
def showAllDetails(*args):
    for data in args:
        s = str(data.__class__)
        type_name = s.split("'")[1].split('.')[1]
        print(f"\n{type_name}'s Details:\n{data}")
        
def displayAllDetails(*args):
    for data in args:
        type_name = data.__class__.__name__
        print(f"\n{type_name}'s Details:\n{data}")
            
if __name__ == '__main__':
    aPerson = Person("Rajan", 1980 )
    print("Person Name : ", aPerson.getName())
    print("Person Year Of Birth : ",aPerson.getYearOfBirth())
    print(aPerson)
    
    aDoctor = Doctor(aPerson, "NeuroSurgen")
    print(aDoctor)
    
    aPerson.setName("Ranjan")
    print(aPerson)
    print(aDoctor)
    
    
    aDoctor.setName("Ranjana")
    print(aDoctor)
    print(aPerson)
    
 
    aPlayer = Player(aPerson, 2004)
    print(aPlayer)
    
    printAllDetails(aPlayer)
    printAllDetails(aDoctor)
    printAllDetails(aDoctor, aPlayer)
    
    printAllDetails(aPerson,aDoctor,aPlayer)
    aPerson.setName("Raju")
    showAllDetails(aPerson,aDoctor,aPlayer)
    aPlayer.setName("Rajesh")
    displayAllDetails(aPerson,aDoctor,aPlayer)
    
    
    del aDoctor
    # print(aDoctor)
    print(aPerson)
    print(aPlayer)
    