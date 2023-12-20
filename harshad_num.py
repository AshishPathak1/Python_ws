import sys
num = input("Enter a integer:")
if not num.isdigit():
    print("Enter valid input ",file=sys.stderr)
    sys.exit(0)
length = len(num)
counter = 0
sum = 0
while counter < length :
    sum = sum + int(num[counter])
    counter = counter + 1
else :
    num = int(num)
    if num % sum == 0:
        print(num,"is a harshad number")
    else:
        print(num,"is not a harshad number")