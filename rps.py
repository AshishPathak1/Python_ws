import random
import sys
from typing import Final
bot_points = 0
user_points = 0
MAX_POINTS:Final[int] = 5
while bot_points < MAX_POINTS and user_points < MAX_POINTS :
    choicelist = ['rock','paper','scissor']
    bot_choice = random.choice(choicelist)
    user_choice = input("Throw!!\n")
    user_choice = user_choice.strip()
    user_choice = user_choice.lower()
    if not user_choice in choicelist :
        print("Enter valid Input",file=sys.stderr)
        sys.exit(0)
    elif bot_choice == user_choice :
        print("Computer goes for :",bot_choice)
        print("Tie")
        print("SCOREBOARD")
        print("Computer = ",bot_points,"\nHumans = ",user_points)
        continue
    else:
        if user_choice == "rock" :
                if bot_choice == "paper" :
                    user_points = user_points + 1
                elif bot_choice == "scissor":
                    bot_points = bot_points + 1
        if user_choice == "paper":
                if bot_choice == 'rock' :
                    user_points = user_points + 1
                elif user_choice == 'scissor':
                    bot_points = bot_points + 1
        if user_choice == "scissor":
                if bot_choice == 'paper' :
                    user_points = user_points + 1
                elif bot_choice == 'rock':
                    bot_points = bot_points + 1
        print("Computer goes for :",bot_choice)
        print("SCOREBOARD\n")
        print("Computer = ",bot_points,"\nHumans = ",user_points)
else :
    if user_points > bot_points:
        print("Hurray! Human wins")
    elif bot_points > user_points:
        print("Hurray! Computer wins")
