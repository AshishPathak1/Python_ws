import sys
from typing import Final

num = input("Enter a positive integer:")

if not(num.isdigit() and int(num) >0):
    print("Enter a valid input ",file = sys.stderr)
    sys.exit(0)

num = int(num)

max_factor :Final[int] = num//2

counter = 2

if(num == 1):
    print(" 1 is neither prime nor composite")
else:
    while(counter <= max_factor ):
        if(num % counter == 0):
            print(num,"is not a prime number ")
            break
        counter = counter + 1
    else:
        print(num,"is a prime number")
