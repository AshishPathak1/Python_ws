import sys

num = input("Enter a positive integer:")

if not num.isdigit() and int(num) <=0 :
    print("Enter a valid input ",file = sys.stderr)
    sys.exit(0)

num = int(num)
print("1")
max_factor  = num//2
counter = 2
while(counter <= max_factor ):
    if(num % counter == 0):
        print(counter)
    counter = counter + 1
print(num)
