# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 08:40:01 2018

@author: Hrishikesh Pisal
"""

# %s format specifier here to tell Python where to 
# substitute the value of name, represented as a string.
name     = "Kajal"
string   = 'Hello, %s'
formatted_string   = string % name # 'Hello, %s' % name
print(formatted_string)

print("Hello ",name,", how are you ?", sep="")

print('Hello %s, How are you?' % name)
print('Hello %s, How are you?' % 'Gauri')

nameList = ["Sarthak", "Shardul", "Sneha", "Shraddha"]

for name in nameList:
    print("Hello %s, Good Evening!" % name)

playerList = ["Jui","Kapil","Harshal","Pranit"]
message = "Hello, %s, How are you?" 
print(message % "Yogita")

for name in playerList:
    print( message % name)
   
menuList = ["Poha", "Upma", "Idly", "Dosa", "Vada"]
for menu_item in menuList:
    print("Enjoy delecious %s!" % menu_item)
    
num = 47806
print('Dec : %d' % num)  ## Dec
#  %x format specifier to convert an int value to a string and to 
#  represent it as a hexadecimal number:
print('Hex : %x' % num)  # Hex
print('Oct : %o' % num)  # Oct
# print('Bin : %b' % num)  # Bin

# print along with base : inappropriate way : error prone
print('Hex with base : 0x%x' % num)  # HEx
print('Oct with base : 0o%o' % num)  # Oct

# print along with base
print('Hex with base : %#x' % num)  # Hex
print('Hex with base : %#X' % num)  # Hex
print('Oct with base : %#o' % num)  # Oct

num = 2000
print('Hex with base : %#x' % num)  # Hex
print('Hex with base : %#X' % num)  # Hex
      
rollNo = 9
name   = "Ketan"
# print("RollNo: %d\tname :%s" % rollNo, name)
print("RollNo: %d\tname :%s" % (rollNo, name))

ip = (192,168,10,149)
print("My systems IP address is %d.%d.%d.%d" % ip)

ip = input("Please enter the Ip Address of your system :")
print("My systems IP address is %s" % ip)

#passing a single tuple as argument
record = (10, "Ketan")
print("RollNo: %d\tname :%s"    % record)
# print("RollNo: %d\tname :%s marks : %f" % record) # Error

# print("RollNo: %d\tname :%s\tRollNo %d" % (rollNo, name))
# positional argument
print("RollNo: %d\tname :%s\tRollNo %d" % (rollNo, name, rollNo))

format_string = "%s's roll number is %d, %s stood first in the class"
print(format_string % ('Ketan',12,'Ketan'))

rollNo = 9
name   = "Leela"
# keyword argument (Mapping Key)
print("RollNo: %(r)d\nname :%(n)s\nRollNo %(r)d" % {"r" : rollNo,"n" : name})

format_string = "%(sname)s's roll number is %(roll)d, %(sname)s stood first in the class"

print(format_string % {"sname":name,"roll":rollNo})

print(format_string %{"sname":"Raja","roll":14})


# keyword argument : order or argument does not matter
print("RollNo: %(roll)d\tname :%(sname)s" % {"sname":name,"roll":rollNo})

sdict = {"sname":"Sandesh",
         "roll":13}
print(format_string % sdict)

#List of Dictionary
records = [{"name":"Monika", "roll":13},
           {"name":"Priti",  "roll":15},
           {"name":"Vedant", "roll":16}]

format_string = "RollNo: %(roll)d\tname :%(name)s"

for a_record in records:
    print(format_string % a_record)
    
mydict = {"apt"  :"apporpriate for that situation",
          "slice":"Cut into pieces"}

print("1st words meaning : %(apt)s\n2nd words meaning : %(slice)s"%mydict)

# Not necessary to use all the keys from the dict
print("1st words meaning : %(apt)s"%mydict)

#Cannot mix the keyword and positional args
num = 999
print("Words meaning : %(apt)s\t%d"%(mydict,num))
print("num = %d\tWords:%(apt)s"%(num,mydict))

# Minimum width Specifier
name = "Rohit"
print("name :|%s|"   % name)
print("name :|%10s|" % name)
print("name :|%3s|"  % name)
name = "Xu"
print("name :|%3s|"  % name)

num = 99
print("Number:|%d|"  % num)
print("Number:|%5d|" % num)
print("Number:|%#5x|" % num)

import math
print(math.pi)  # 15
# %f : six digit precision 
print('|%f|'   % math.pi)   # 6
print('|%10f|' % math.pi) #minimum width specifier


# Controlling Precision
pi = math.pi
print("Real number = ", pi)
#Rounds the value upto six digit precision
print("Real number = %f "   % pi)
print("Real number = %.2f " % pi)
print("Real number = %.0f " % pi)
print("Real number = %.4f " % pi)

real = 1.6789
print("Real number = %.2f " % real)
print("Real number = %.0f " % real)

# using specifiers in combination
print("Real number= |%f|"       % pi)
print("Real number= |%10f|"     % pi) # minimum field width specifier
print("Real number= |%.2f|"     % pi) # precision specifier
print("Real number= |%10.2f| "  % pi) # Combination of specifiers

real = 120000000000.0

print("Real Number =",     real)
print("Real Number = %F" % real)
print("Real Number = %f" % real)
print("Real Number = %e" % real) #exponantial format with six digit percision
print("Real Number = %E" % real)
print("Real Number = %g" % real) #exponantial format with only significant 
print("Real Number = %G" % real) #digit after the decimal point

real = 3.4
print("Real Number = %F" % real)
print("Real Number = %e" % real)
print("Real Number = %G" % real) #fixed/exponantial format which ever is shorter

real = 123000000000.0
print("Real Number = %e"   % real)
print("Real Number = %.2e" % real)
print("Real Number = %.4e" % real)

#  Character formatting
# using variable
ch = 'A'
print("Character = %c " % ch)

# using constant
print("Character = %c" % 'Q')     #char
print("Character = %c" % 224)     #int
print("Character = %c" % 1108)    #int
print("Character = %c" % 2309)  
print("Character = %c" % 8486)   # \u2126
print("Character = %c" % 0x2126)   # \u2126
print("Character = %c" % 0x00A3)   # \u2126
print("Character = %c" % 136.67)  #real Error
print("Character = %c" % 'UML')   #String Error

# using code
val = 65
print("Character = %c" % val)
print("Character = %d" % val)

val = 'R'
print("Character = %c" % val)
print("Character = %d" % val) #error
print("Character = %d" % ord(val)) 

# flag "+" in format directive to specify sign
num = -44
print("Number = %d" % num)
num = +44
print("Number = %d" % num)
num = 44
print("Number = %+d" % num)
num = -44
print("Number = %+d" % num)

# Padding space with 0
num = 43
print("Number = |%5d|"  % num)
print("Number = |%05d|" % num)
import math
print("PI = |%010.2f|"%math.pi)

# Left justification (default is right)
num = 43
print("Number = |%5d|"   % num)
print("Number = |%05d|"  % num)
print("Number = |%-5d|"  % num)
print("Number = |%-05d|" % num) 

name = "Raj"
print("name:|%10s|"  %name)
print("name:|%-10s|" %name)


# Precedes a positive number with a blank space
print("%d%d" % (-10, 10))
print("% d% d" % (-10, 10))
print("%   d%   d" % (-10, 10))
print("%d %d" % (-10, 10))
print("%d    %d" % (-10, 10))

# String % Dictionary

record = {
           "occupation" : "Chef",
           "name"       : "Mohan",
           "income"     : 40000.34534
        }

print("%(name)s is a %(occupation)s earning Rs%(income) -10.0f" % record)

print("income = Rs %(income)-13.2f" % record)
print("income = Rs %(income)13.2f"  % record)

per = 75.8975
print("My percentage score is %.2f%% grade point" % per)

# width specifier supplied at runtime
num   = int(input("Enter a number:"))
width = int(input("How much width to use:"))
print("Value = |%*d|" % (width, num))

# width and precision specifier supplied at runtime
num       = float(input("Enter a real number:"))
width     = int(input("How much width to use:"))
pricision = int(input("What should be the precesion?"))

print("Value = %0*.*f" % (width, pricision, num))

print("Gold    = ",123456.7845)
print("Copper  = ",456.3244)
print("Silver  = ",1456.38)
print("total   = ",(123456.7845+456.3244+1456.38))

product = [
        {"name": 'Gold',   "price" :   123456.7845},
        {"name": 'Copper', "price" :   456.3244},
        {"name": 'Silver', "price" :   1456.38}
        ]

# Screen formatting
print()
line = '-'*21
print(line)
print("   ****  Bill  ****")
print(line)  
format_string = "%(name)-7s = %(price)10.2f"
total_price = 0
for record in product:
    print(format_string % record)
    total_price += record["price"]
  
format_string = "%-7s = %10.2f"
print(line)
print(format_string % ("Total",total_price))
print(line)

# redirect to File
print()
myfile = open('d:/temp/report.txt','w')
line = '-'*21
print(line,file=myfile)
print("   ****  Bill  ****",file=myfile)
print(line,file=myfile)  
format_string = "%(name)-7s = %(price)10.2f"
total_price = 0

for record in product:
    print(format_string % record,file=myfile)
    total_price += record["price"]
  
format_string = "%-7s = %10.2f"
print(line,file=myfile)
print(format_string % ("Total",total_price),file=myfile)
print(line,file=myfile)
myfile.close()
