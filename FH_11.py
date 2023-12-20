# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:34:27 2019

@author: Hrishikesh Pisal
"""

from random import randint 

def demoReadWriteNumbers():
    # Open file for writing data
    outfile = open("Numbers.txt", "w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close() # Close the file

    # Open file for reading data
    infile = open("Numbers.txt", "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    print(numbers)
	
    for number in numbers:
        print(number, end = " ")
    infile.close() # Close the file
    
if __name__ == '__main__':    
    demoReadWriteNumbers() # Call the main function
