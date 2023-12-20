# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:28:38 2023

@author: hrish
"""
import sys 

def add(a:int, b:int)->int:
    """+"""
    return a + b

def multiply(a:int, b:int)->int:
    """x"""
    return a * b

def divide(a:int, b:int)->int:
    """/"""
    return a / b if b != 0 else "Cannot divide by zero"

def power(a:int, b:int)->int:
    """^"""
    return a ** b

def printMenu()->None:
    print("\nMenu of Operations:")
    print("1. Addition\n2. Multiplication\n3. Division\n4. Power\n5. Stop")
    
    
def acceptMenuChoice():
    while True:
        choice = input("Enter your choice from above list (1/2/3/4/5): ")
        if not choice.isdigit():
            print("Enter the input in a valid format!", file=sys.stderr)
            continue
        choice = int(choice)
        if choice not in range(1,6):
            print("Your choice has to be in the range of 1 to 5")
            continue
        break
    return choice


def acceptInteger(msg:str)->int:
    num = input(msg)
    if not num.isdigit():
        print("Enter the input in a valid format!", file=sys.stderr)
        sys.exit(0)
    return int(num)

def stop()->None:
    print("That's all!")
    
if __name__ == "__main__":
    
    operations = {
                    1 : add,
                    2 : multiply,
                    3 : divide,
                    4 : power,
                    5 : stop
                 }

    while True:
        printMenu()
        choice = acceptMenuChoice()
        print()
        if choice == 5:
            stop()
            break
        
        if choice in operations:
                num1 = acceptInteger("Enter the first Integer : ")
                num2 = acceptInteger("Enter the second Integer : ")
                result = operations[choice](num1, num2) #indirect call
                print(f"{num1} {operations[choice].__doc__} {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid option.")
