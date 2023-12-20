# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 08:47:21 2019

@author: Hrishikesh Pisal
"""

class Rectangle:
    
    def __init__(self, length, breadth):
        print("...creating object...")
        if  length > 0:
            self.__length = length
        else:
            self.__length = 1
        
        if  breadth > 0:
            self.__breadth = breadth
        else:
            self.__breadth = 1
            
       
    @property
    def length(self):
        return self.__length
    
  
    @length.setter
    def length(self, length):
        if(isinstance(length,(int, float))):
            if  length <= 0:
                print("Length not updated!")
            else:
                self.__length = length
        else:
            print("Value of length should be numeric ")
                
    @property
    def breadth(self):
        return self.__breadth
          
    @breadth.setter   
    def breadth(self, breadth):
        if(isinstance(breadth,(int, float))):
            if  breadth <= 0:
                print("breadth not updated!")
            else:
                self.__breadth = breadth
        else:
            print("Value of breadth should be numeric ")
            
    @property
    def area(self):
        return (self.__length * self.__breadth)
    
    def __str__(self):
        return f"\n\tlength : {self.__length} \n\tbreadth  : {self.__breadth}" 
    
if __name__ == "__main__":
    rectangle1 = Rectangle(10,20)
    print("Rectangle 1 ", rectangle1 )
    print("Rectangle 1 Area :", rectangle1.area)
    
    rectangle1.length = 44
    rectangle1.length = -4
    rectangle1.breadth  = 55
    print("Rectangle 1 ", rectangle1 )
    print("Area of Rectangle : ", rectangle1.area)
    
    rectangle2 = Rectangle(-20,40)
    print("Rectangle 2 ", rectangle2 )
    
    rectangle2.length = -4
 
    print("Rectangle 2 ", rectangle2 )
    rectangle2.length = 55
    rectangle2.breadth = 65
    print("Rectangle 2 ", rectangle2 )
    
    print("Rectangle 2 length : ",rectangle2.length, "breadth : ",rectangle2.breadth)

# Traditional
    # rectangle2.setlength(33)
    # rectangle2.setbreadth(44)
    # print("Rectangle 2 length : ",rectangle2.getlength(), "breadth : ",rectangle2.getbreadth())
  