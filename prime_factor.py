import sys
import math
num = input("Enter a positive integer:")

if not num.isdigit() and int(num) <=0 :
    print("Enter a valid input ",file = sys.stderr)
    sys.exit(0)

num = int(num)
max_factor  = num//2
counter = 2
cntr = 2
while counter <= max_factor :
    if num % counter == 0 :
        while cntr <= counter // 2:
            if counter % cntr == 0 :
                break
            else:
                cntr = cntr + 1
        else:
            print(counter)
    counter = counter + 1