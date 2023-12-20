# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:58:32 2020

@author: Hrishikesh Pisal
"""
# Dynamic Binding (Polmorphism)

class Student:
    
    def __init__(self,name:str):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def __str__(self):
       return f"Name : {self.__name}"

    def printStudent(self):
       print(self.__str__()) 
    
    def getStudentDetails(self):
        raise NotImplementedError("Service implementation not provided for this class")     
       
# end of Student Class declaration

class GraduateStudent(Student):
    
    def __init__(self,name:str,degree:str):
        super().__init__(name)
        self.__degree = degree
    
    def __str__(self):
       return super().__str__() + " Degree :"+ self.__degree

    def getStudentDetails(self):
        print(f"{self.getName()} is a Graduate Student")  
        
# end of GraduateStudent Class declaration

class UnderGraduateStudent(Student):
    def __str__(self):
       return "Under Graduate Student"
   
    def getStudentDetails(self):
        print(f"{self.getName()} is a Under Graduate Student")  

# end of UnderGraduateStudent Class declaration

def who_is_it(astudent:Student):
    astudent.getStudentDetails()
    
if __name__ == '__main__':
    # a = Student("Atharva")
    # a.getStudentDetails()
    # a.printStudent()
    
    gs = GraduateStudent("Avinash","BCA")
    gs.getStudentDetails()
    gs.printStudent()
    
    ug = UnderGraduateStudent("Sanjay")
    ug.getStudentDetails()
    ug.printStudent()
    
    
    studentList = [gs,ug]
    for astudent in studentList:
        who_is_it(astudent)
     
    who_is_it(gs)
    who_is_it(ug)
    

    who_is_it(studentList)  #Error
    who_is_it(34) # Error
    