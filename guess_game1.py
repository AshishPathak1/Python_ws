import random
import sys
from typing import Final
result = random.randint(0,101)
MAX_ATTEMPT:Final[int] = 5
counter = 1
while counter <= MAX_ATTEMPT :
    guess = input("Enter your guess;:")
    if not guess.isdigit()  :
        print('Enter an integer in range 0 to 100',file=sys.stderr)
        sys.exit(0)
    if not int(guess) in range(101) :
        print("Enter number in range 0 to 100",file=sys.stderr)
        sys.exit(0)
    guess = int(guess)
    if guess == result :
        print("CONGRATULATIONS !!\nYou won !!")
        break
    elif guess < result :
        print("result is grester than ",guess)
    elif guess > result :
        print("result is lesser than",guess)
    counter = counter + 1
    print((MAX_ATTEMPT - counter + 1),"attempts remaining")
else :
    print("GAME OVER!!\nYou Lost")
    print("The number was",result)