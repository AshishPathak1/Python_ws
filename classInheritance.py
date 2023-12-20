# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:55:32 2019

@author: Hrishikesh Pisal
"""


# class Student(object): # 2.X

class Student:
    
    def __init__(self, name, roll):
        if not Student.__isNameValid(name):
            raise ValueError("Name supplied is invalid")
        if not Student.__isRollNoValid(roll):
            raise ValueError("Roll number is invalid")
        self.__name = name
        self.__roll = roll
        
    def getName(self):
        return self.__name

    def getRoll(self):
        return self.__roll

    def __str__(self):
        return f"{self.__name} has roll number {self.__roll} "
    
    def __repr__(self):
        return f"Name :{self.__name}\t Roll No : {self.__roll} "
    
    @staticmethod
    def __isRollNoValid(roll):
        if isinstance(roll,int):
            if roll > 0:
                return True
        return False
      
    @staticmethod
    def __isNameValid(name):
        if isinstance(name,str):
            if name.isalpha():
                return True
        return False
    


class PG_Student(Student):
    
    def __init__(self, tname, troll, tspecialization):
        super().__init__(tname, troll)
        self.__specialization = tspecialization
 
    
    def __str__(self):
        # d = super().getRoll()  # ok : Public
        # d = self.__roll    # private
        # d = super().__isNameValid("sdf")   # private
        return f"{super().__str__()} with Specialization: {self.__specialization} "

    def getSpecialization(self):
        return self.__specialization

    def setSpecialization(self, specialization):
        self.__specialization = specialization


 

if __name__ == '__main__':
    student = Student("Harsh", 12)
    
    # print("Name   : ", student.getName())
    # print("Roll No: ", student.getRoll())
    # print(student)

    pg_student = PG_Student("Sujay", 25, "ThermoDynamics")
   
    print(pg_student)
    print(pg_student.getName())
    print(pg_student.getRoll())
    print(pg_student.getSpecialization())
   
  
   
    # print(Student.__isNameValid("Raja"))
    # print(PG_Student.__isNameValid("Raja"))
    # print(s2.__isNameValid("Raja"))
    