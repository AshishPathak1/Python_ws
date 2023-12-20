# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 09:15:41 2018

@author: Hrishikesh Pisal
"""

## iter Parameters
## iter with sentinal value

text = "Failure will never overtake me if my determination"\
" to succeed is strong enough"

print(text)

print(text.__iter__)

letter_iterator = iter(text)
print(f"Iterator Type {letter_iterator}") # str_iterator

for letter in letter_iterator:
    print(letter)
    
    
word_list = text.split()
for word in word_list:
    print(word)    

    
word_list = text.split()
word_iter = iter(word_list)
print(word_iter.__next__())
for word in word_iter:
    print(word)    


for word in text.split():
    print(word)

word_iterator = iter(text.split())
print(f"Iterator Type {word_iterator}") #list_iterator

for word in word_iterator:
    print(word)
 
word_list = ["happy","sad","fun","game","flower"]
word_iterator = iter(word_list)
# this iterator stops when all elements have been iterated
for word in word_iterator:
    print(word)


word_list = ["happy","sad","fun","game","flower","fruit"]
# If the second argument, sentinel, is given, 
# then object must be a callable object
word_iterator = iter(word_list.pop,"sad")
# callable_iterator
print(f"Iterator Type {word_iterator}") # callable_iterator 

for word in word_iterator:
    print(word)

    
#iterates till end
myfile = open("d:/python/programs/data.txt","r")
file_iterator = iter(myfile)
print(f"Iterator Type {file_iterator}") 

for line in file_iterator:
    print(line,end="")
    
    
    
#using second parameter in iter (sentinal)
myfile = open("d:/python/programs/data.txt","r")
file_iterator = iter(myfile.readline,'end\n')
print(f"Type : {type(file_iterator)}")
for word in file_iterator:
    print(word,end="")
    