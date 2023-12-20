# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:33:11 2023

@author: hrish
"""

class Circle:
    from typing import Final
    MIN_RADIUS:Final[float] = 0.0
    
    def is_radius_valid(radius:float)->bool:
        if not isinstance(radius, (int,float)):
            raise TypeError("Radius should be numeric value")
            
        if radius > Circle.MIN_RADIUS:
            return True
        else:
            raise ValueError("The Radius should be > 0.0")
        
    def __init__(self, radius:float = 1.0):
        self.setRadius(radius)
    
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius:float)->None:
        if Circle.is_radius_valid(radius):
            self.radius = radius
         
    def getArea(self)->float:
        import math
        area = math.pi * (self.radius**2)
        return area
    
    def getPerimeter(self)->float:
        import math
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
if __name__ =='__main__':
    try:
        circle1 = Circle(4)
        print(f"Radius of cirlce1    = {circle1.getRadius():.2f}")
        print(f"Area of cirlce1      = {circle1.getArea():.2f}")
        print(f"Perimeter of circle1 = {circle1.getPerimeter():.2f}")
        
        circle1.setRadius(4)
        print(f"Area of cirlce1      = {circle1.getArea():.2f}")
        print(f"Perimeter of cirlce1 = {circle1.getPerimeter():.2f}")
        
        
        circle2 = Circle(25)
        print(f"Area of cirlce2      = {circle2.getArea():.2f}")
        print(f"Perimeter of cirlce2 = {circle2.getPerimeter():.2f}")
        
        
        circle3 = Circle(12)
        print(f"Area of cirlce3      = {circle3.getArea():.2f}")
        print(f"Perimeter of cirlce3 = {circle3.getPerimeter():.2f}")
    except (ValueError,TypeError) as err:
        print(f"{type(err).__name__} : {err}")