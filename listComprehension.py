# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:06:13 2021

@author: Hrishikesh Pisal
"""
# Construct List - I ( First 4 even nos)
numberList = [2,4,6,8]
for number in numberList:
    print(number)

print(numberList)

names= ["Milan","leela","pooja","Shri"]
print("\n".join(names))
for name in enumerate(names,start=1):
    print(f"{name[0]}.{name[1]}")

# Construct List - II ( First 4 even nos)
evenSet = {2,4,6,8,10}
numberList = list(evenSet) 
for number in numberList:
    print(number)
    
# Construct List - III ( First 10 even nos)
numberList = list(range(2,21,2))
for number in numberList:
    print(number)
  
# Construct List -IV (1,4,9,16,25,36)

numberList = []
for number in range(1,11):
    numberList.append(number**2)
print(numberList)    


# List Comprehension
   
numberList = [number**2 for number in range(1,11)]
print(numberList)
 

marks = 66
if(marks >= 35):
    print("Pass")
else:
    print("Fail")

print("pass") if(marks >= 35) else print("Fail")