import sys
from typing import Final

MIN_FACTOR :Final[int] = 1

num = input("Enter a positive integer:")


if not(num.isdigit() and int(num) >0):
    print("Enter a valid input ",file = sys.stderr)
    sys.exit(0)

num = int(num)

MAX_FACTOR :Final[int] = num//2

counter = 2
print(MIN_FACTOR ,"is factor of ", num)
while(counter <= MAX_FACTOR ):
    if(num % counter == 0):
        print(counter ,"is a factor of ", num )
    counter = counter + 1
print(num ,"is a factor of ",num)