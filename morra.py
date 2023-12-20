import random
import sys
from typing import Final
MAX_POINTS:Final[int] = 5
bot_points =0
user_points =0
while bot_points < MAX_POINTS and user_points < MAX_POINTS :
    guesslist = [0,1,2,3]
    sumlist = [0,1,2,3,4,5,6]
    bot_guess = random.choice(guesslist)
    bot_sum_guess = random.choice(sumlist)
    user_guess = input("Throw!!")
    user_guess = user_guess.strip()
    if not user_guess.isdigit() :
        print("Enter valid Input!!",file = sys.stderr)
        sys.exit(0)
    user_guess = int(user_guess)
    if not user_guess in guesslist:
        print("Enter valid Input",file=sys.stderr)
        sys.exit(0)
    user_sum_guess = input("Enter the sum guess:")
    if not user_sum_guess.isdigit() :
        print("Enter valid Input!!",file = sys.stderr)
        sys.exit(0)
    user_sum_guess=user_sum_guess.strip()
    user_sum_guess = int(user_sum_guess)
    if not user_sum_guess in sumlist:
        print("Enter valid Input",file=sys.stderr)
        sys.exit(0)
    sum = bot_guess + user_guess
    if bot_sum_guess == user_sum_guess == sum :
        print("Tie!!")
    elif bot_sum_guess == sum :
        print("Computer wins!!")
        bot_points = bot_points + 1
    elif user_sum_guess == sum :
        print("Human wins!!")
        user_points = user_points + 1
    else:
        print("Bad luck !! Try Again")
    print(bot_guess)
    print(bot_sum_guess)
    print("SCOREBOARD:")
    print("Computer = ",bot_points,"\nHumans = ",user_points)

if bot_points < user_points:
    print("Hurray! Human wins")
else:
    print("Hurray! Computer wins")