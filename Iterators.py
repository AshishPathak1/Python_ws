# Iterators

# We use for statement for looping over a list.
print('Iterating over list')
for element in [1, 2, 3, 4]:
    print(element)

#If we use it with a string, it loops over its characters.
print('Iterating over characters in the String')
for char in "python":
    print(char)

#If we use it with a dictionary, it loops over its keys.
print('Iterating over keys in the dictionary')
for k in {"x": 1, "y": 2}:
     print(k)
     
playerDict = {'Sachin':101,'Saurav':48,'Rahul':65}

for name,centuries in playerDict.items():
     print(f'{name} has scored {centuries} centuries')

# If we use it with a file, it loops over lines of the file.
print('Iterating over lines in the file')
for line in open("data.txt"):
    print(line,end="")

player_list = ['Sachin','Saurav','Rahul','Anil','Javagal']
print('List of player_list (using for loop1):')
for player in player_list:
    print(player)

player_list = ['Sachin','Saurav','Rahul','Anil','Javagal']

# get the iterator of the player list   
 
playerIter = iter(player_list)
print(playerIter) # List_iterator
print('List of players (using iterator):')
# elements in in linear order
# fetch next element from the list using iterator
print(next(playerIter))
print(next(playerIter))
print(next(playerIter))
print(next(playerIter))
print(next(playerIter))
print(next(playerIter))

#elements are in hierarchial order
playerDict = {'Sachin':101,'Saurav':48,'Rahul':65}

playerIter = iter(playerDict)
print(playerIter)
print(next(playerIter))


iterator = iter("Python")
print(iterator)
print(iterator.__next__())


alist1 = [2,4,6,8]
alist2 = ["two", "four", "six", "eight"]


data = zip(alist1,alist2)

print(type(data))

print(data)
for ele in data:
    print(ele)
   
data = zip(alist1,alist2)
zipiter = iter(data)
print(zipiter)
print(next(zipiter))
print(zipiter.__next__())


odd_nums = range(1,10,2)
for odd in odd_nums:
    print(odd)

riter = iter(range(1,10,2))
print(f"Range iterator : {type(riter)}")
print(next(riter))
print(riter.__next__())

import random

r = random.randint(10, 100)
print(r)




