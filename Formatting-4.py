# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 08:18:13 2019

@author: Hrishikesh Pisal
"""

name   = "Ramesh"
age    = 45

result = f"Hello, {name}. You are {age}."

print(result)

# using Expression
a = 5
b = 6
print(f"{a} * {b} = {a*b}")
print(F"{a} + {b} = {a+b}")

name = "Tiger Shroff"
print(f"Name = {name}")

# Calling Function
print(f"Your name {name.lower()} is funny")
print(f"Your name {name.upper()} is funny")

# Why %-formatting Isn’t Great
# The code examples that you just saw above are readable enough.
#
first_name  = "Leela"
last_name   = "Patil"
age         = 27
profession  = "Professor"
affiliation = "Pune Univ"

print("Hello, %s %s. You are %d. You are a %s. "\
      "You were a member of %s."
      %(first_name, last_name, age, profession, affiliation))
    
# Why str.format() Isn’t Great
# Code using str.format() is much more easily readable than 
# code using %-formatting, but str.format() can still be quite 
# verbose when you are dealing with multiple parameters and longer strings.

first_name  = "Leela"
last_name   = "Kulkarni"
age         = 30
profession  = "Professor"
affiliation = "pune univ"

# using positional (index) argumnet
print(("Hello, {0} {2}. You are {1}. " + 
      "You are a {3}. You were a member of {4}.") \
       .format(first_name, age, last_name, profession, affiliation))

#using keyword argument
print(("Hello, {fname} {lname}. You are {age}. " + 
      "You are a {profession}. You were a member of {affiliation}.") \
       .format(fname      = first_name,     \
               age        = age,            \
               lname      = last_name,      \
               profession = profession,     \
               affiliation= affiliation))

print(f"Hello, {first_name} {last_name}. "  \
      f"You are {age+1}. "                  \
      f"You are a {profession}. "           \
      f"You were a member of {affiliation.title()}.")

# Formatting multiline Strings within parenthesis 
# without line continuation character
message = ( f"Hello, {first_name} {last_name}. "  
            f"You are a {profession}. "
            f"You were in {affiliation.title()}."
          )
print(message)

# Formatting multiline Strings without parenthesis 
message = f"Hello, {first_name} {last_name}. "  \
          f"You are a {profession}. "           \
          f"You were in {affiliation.title()}."
   
print(message)


#  This module provides a simple way to time small bits of Python code.
#  Measure execution time of small code snippets
import timeit  

# Performance of f-string

mystatement ='''name = "Jonny" 
age = 74
'%s is %d.' %(name, age)'''
                              
print("using %",timeit.timeit(stmt=mystatement,number=2000000))

mystatement = 'format("Jonny","s") + " is " + format(31,"d")'
                              
print("using format function",timeit.timeit(stmt=mystatement,number=2000000))

mystatement='''name = "Jonny"
age = 74
'{0} is {1}.'.format(name, age)'''

print("using str.format",timeit.timeit(stmt=mystatement,number=2000000))


mystatement="""name = "Jonny" 
age = 74
f'{name} is {age}.'"""

print("using f",timeit.timeit(stmt=mystatement,number=2000000))

# Test on command prompt
# python3 -m timeit -u msec '"-".join(str(n) for n in range(100))'

print("** Quotation Marks **")

# message = f'{Jonny Lever}' #error
print(message)

message = f'{"Jonny Lever"}'
print(message)

message = f'\"{"Jonny Lever"}\"'
print(message)

message = f'"{"Jonny Lever"}"'
print(message)

message = f"\'{'Jonny Lever'}\'"
print(message)

message = f"'{'Jonny Lever'}'"
print(message)


message = f"""'{"Jonny Lever"}' 
'{"Laxman"}'"""
print(message)


# Following 5 styles are not preferred
message = f'\"Jonny Lever\"'
print(message)

message = f'"Jonny Lever"'
print(message)

# message = f''Jonny Lever''
# print(message)

message = f'\'{"Jonny Lever"}\''
print(message)

message = f"'{'Jonny Lever'}'"
print(message)

message = f"""'Jonny Lever'
'Laxman'"""
print(message)

# %-formatting cannot handle tuple or dictionary

#using F-string with dictionaries

player = {'name': 'Saurav Ganguli', 'age': 47}

# Avoid this way to get data from dictionary
print(player['name'])
# print(player['weight'])

# Better way to get data from dictionary
print(player.get('name'))
print(player.get('weight'))

# Best way to get data from dictionary
print(player.get('name',"Not known"))
print(player.get('weight',"Not known"))

s = f"The player {player['name']}, is aged {player['age']}."
print(s)

# s = f"The player {player['name']}, has weight {player['weight']}."
# print(s)


s = f"The player {player.get('name')}, is aged {player.get('age','Not known')}."
print(s)

s = f"The player {player.get('name')}, weight is {player.get('weight','Not known')}."
print(s)


#String literals also support the existing format string syntax 
#of the str.format() method
errno = 1234
name  = 'Kapil'
print(f"Hey {name}, there's a {errno:#d} error!")
print(f"Hey {name}, there's a {errno:#x} error!")
print(f"Hey {name}, there's a {errno:#b} error!")
print(f"Hey {name}, there's a {errno:#o} error!")
print(f"Hey {name}, there's a |{errno:10d}| error!")

avgScore = 45.6789
print(f"Average Score is {avgScore}")
print(f"Average Score is {avgScore:.2f}")
print(f"Average Score is |{avgScore:10.2f}|")
print(f"Average Score is |{avgScore:#^10.2f}|")
print(f"Average Score is |{avgScore:#<10.2f}|")
print(f"Average Score is |{avgScore:#>10.2f}|")


name = "Raj"
print(f"name")
print(f"{name}")

num1 = 10
num2 = 20
print(f"num1")
print(f"{num1}")

print(f"num1 + num2 = num1 + num2")
print(f"{num1} + {num2} = {num1 + num2}")


# Braces
print(f"74")   # 0 Braces

print(f"{74}")   # 1 Braces

print(f"{{74}}")   # 2 Braces
 
print(f"{{{74}}}")  # 3 Braces
 
print(f"{{{{74}}}}") # 4 Braces

print(f"{{{{{74}}}}}") # 5 Braces

print(f"{{{{{{74}}}}}}") # 6 Braces

table = {'Bobby': 4127, 'Avinash': 4098, 'Gaurav': 7678}

for name, emp_id in table.items():
    print(f'{name:10}==>{emp_id:10d}')

for name, emp_id in table.items():
    print(f'{name:10}==>{emp_id:10d}', file=open("aman.txt","a"))    
