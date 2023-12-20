# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:54:45 2018
Send Method with Generator
@author: Hrishikesh Pisal
"""

#Send method
# Sending a message, i.e. an object, into the generator can
# be achieved by applying the send method to the generator 
# object.


def getValues():
    val = yield 0
    val = yield(val**2)
    val = yield(val**3)
    val = yield(val**4)

  
def getSquare():
    while True:
        print('1')
        val = yield  
        print('2')
        yield (val * val)

if __name__ == '__main__':
    gen = getValues()
    result = next(gen)
    print(result)
    result = gen.send(2)
    print("Value=> 2 :",result)
    result = gen.send(13)
    print("Value=> 3 :",result)
    result = gen.send(4)
    print("Value=> 4 :",result)
    
    gene = getSquare()
    result = next(gene)
    print(result)
    
    result = gene.send(10)
    print("Send 10:", result )
    result = next(gene)
    print(result)
    
   
    result = gene.send(10.5)
    print("Send 10.5:", result )
    result = next(gene)
    print(result)
    
    result = gene.send('A')
    print("Send 'A':", result )
 
