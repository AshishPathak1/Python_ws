# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:23:43 2023

@author: hrish
"""

class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx)
    
if __name__ == '__main__':
    obj1 = C()
    obj1.setx(44)
    print(f"x = {obj1.getx()}")
    # obj1.delx()
    # print(f"x = {obj1.getx()}")
    
    print(f"What's x ? : {obj1.x.doc}")
    obj1.x = 99
    print(f"x = {obj1.x}")
    del obj1.x