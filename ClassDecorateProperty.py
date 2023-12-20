# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:07:26 2019

@author: Hrishikesh Pisal
"""

class Student:
    def __init__(self, firstName, lastName, roll):
        #following attributes will be attached
        #to every object of Student type
        self._firstName = firstName
        self._lastName  = lastName
        self._roll      = roll
    # end of __int__
   
    def _isNameValid(self,name):
        return isinstance(name,str) and name.isalpha()
    
    @property
    def firstname(self):
        return self._firstName
    
    @property
    def lastname(self):
       return self._lastName
    
    @property
    def roll(self):
        return self._roll
    
    @firstname.setter
    def firstname(self,fname):
       if self._isNameValid(fname):
           self._firstName = fname
       else:
           print("Name supplied has to be only String")
        
    @lastname.setter
    def lastname(self,lname):
       if self._isNameValid(lname):
           self._lastName = lname  
       else:
           print("Name supplied has to be only String")    
         
    @roll.setter
    def roll(self,new_roll):
       if (isinstance(new_roll,int) and new_roll > 0):
           self._roll = new_roll
           
    @property
    def fullname(self):
        return f"{self._firstName} {self._lastName}"
    
    @fullname.setter
    def fullname(self,full_name):
        fname,lname = full_name.split()
        
        if self._isNameValid(fname):
            self._firstName = fname
            
        if self._isNameValid(lname):
            self._lastName = lname
    
    def __str__(self):
        return f"{self._firstName} {self._lastName} has Roll No.: {self._roll}"
    
#end of the class definition


if __name__ == '__main__':
    s1 = Student("Rama","Rao",12)
    print("First Name : ", s1.firstname)
    print("Last Name  : ", s1.lastname)
    print("Roll Number: ", s1.roll)
    
    s1.firstname = 45.67
    s1.firstname = "45.67"
    s1.firstname = "Salim"
    s1.lastname  = "Khan"
    print("First Name : ", s1.firstname)
    print("Last Name  : ", s1.lastname)
    print("Roll Number: ", s1.roll)
    
    s1.fullname = "Ramkrishna Pandit"
    print("First Name : ", s1.firstname)
    print("Last Name  : ", s1.lastname)
    print("Roll Number: ", s1.roll)
    print("Full Name  : ", s1.fullname)

    print("Student Details \n",s1)