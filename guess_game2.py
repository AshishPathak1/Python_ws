import random
import sys
from typing import Final
import time
result = random.randint(1,101)
MAX_ATTEMPT:Final[int] = 5
prev_time =  int(time.time())
new_time = 0 
while new_time - prev_time < 25 :
    guess = input("Enter your guess;:")
    new_time =  int(time.time())
    if not guess.isdigit()  :
        print('Enter an integer in range 0 to 100',file=sys.stderr)
        sys.exit(0)
    if not int(guess) in range(1,101) :
        print("Enter number in range 0 to 100",file=sys.stderr)
        sys.exit(0)
    guess = int(guess)
    if guess == result :
        print("CONGRATULATIONS !!\nYou won !!")
        print("You took ",(new_time - prev_time),"seconds !!")
        break
    elif guess < result :
        print("result is greater than ",guess)
        continue
    elif guess > result :
        print("result is lesser than",guess)
        continue
    
else :
    print("GAME OVER!!\nYou Lost")
    print("The number was",result)