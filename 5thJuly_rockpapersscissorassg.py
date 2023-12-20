import random

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, and 2 for Scissors (or enter 5 to quit): "))

while user_choice != 5:
    if user_choice not in [0, 1, 2]:
        print("Please choose either 0, 1, or 2 to continue playing.")
    else:
        computer_choice = random.randint(0, 2)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a draw.")
        elif user_choice == 0 and computer_choice == 2:
            print("You win! You chose Rock and the computer opted for Scissors.")
        elif user_choice == 1 and computer_choice == 0:
            print("You win! You chose Paper and the computer opted for Rock.")
        elif user_choice == 2 and computer_choice == 1:
            print("You win! You chose Scissors and the computer opted for Paper.")
        else:
            print("You lose.")

    user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, and 2 for Scissors (or enter 5 to quit): "))

print("You opted to quit,See you next time!")

