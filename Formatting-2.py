# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:46:22 2020

@author: Hrishikesh Pisal
"""

num = 65535

print('Dec : %d' % num)  ## Dec
print('Dec :',format(num,"d"))

formatted_output = format(num,"d")
print('Dec :'+formatted_output)

#  %x format specifier to convert an int value to a string and to 
#  represent it as a hexadecimal number:
print('Hex : %#x' % num)  # Hex
print('Hex :', format(num,"#x"))

print('Oct : %#o' % num)  # Oct
print('Oct :', format(num,"#o"))

# print('Bin : %b' % num)  # Bin #Error
print(format(num, 'b'))
print(format(15, 'b')) # Binary
print(format(10, '#b')) # Binary
print(format(55, '#b')) # Binary

# print along with base
num = 2000
print('Hex with base : %#x' % num)  # HEx
print('Hex with base :',format(num,"#x")) # HEx

print('Oct with base : %#o' % num)  # Oct
print('Oct with base :',format(num,"#o")) # Oct
print('Bin with base :',format(num,"#b"))
      
roll    = 9
sname   = "Sujay"

print("RollNo: %d\tName : %s" % (roll, sname))

print("RollNo:", format(roll,"d"), "\tName :",format(sname,"s"))


# integers
print(format(-10, '+')) # With sign
print(format( 10, '+')) # With sign

print(format(-10, '+d')) # With sign
print(format( 10, '+d')) # With sign

# Width specifier
print(format(55, '10d')) # width Without sign
print(format(55, '+10d'))
print(format(55, '+10')) # width With sign
#sign alignment
print(format(55, '=+10'))
print(format(55, '=+010'))
print(format(55, '*=+10'))
print(format(55, '#=+10'))


#Alignment
# make a string center-aligned , '^' symbol
print(format("Hello", "#^15s"))
print(format("Goodday!", "#^15s"))

# align the target string from the left,  ‘<‘ symbol.   
print(format("Hello", "#<10s"))

# align the target string from the right,  ‘>‘ symbol.   Hello
print(format("Hello", "#>10s"))

# pad internal blank spaces to numeric values
num = 55
print(format(num, '#=+10'))
num = -55
print(format(num, '#=+10'))
print(format(num, '*=+10'))
print(format(num, '*^+10'))
print(format(num, '*<+10'))
print(format(num, '*>+10'))

# float
print(format(0.20, '%')) # X 100
print(format(0.10, '%')) # X 100
print(format(0.45, '.2%'))
print(format(0.105, '.2%'))

print(format(10.5, 'e'))
print(format(10.5, 'E'))
print(format(10500000, 'e'))
print(format(10500000, 'E'))
print(format(10500000, 'g'))
print(format(10500000, 'G'))
print(format(0.00005, 'g'))
print(format(0.00005, 'G'))


print(format(10.5345679, 'f'))
print(format(10.5345679, 'F'))

print(format(10.5345679, '10.2F'))
print(format(10.5345679, '010.2F'))
print(format(10.5345679, '#<10.2F'))