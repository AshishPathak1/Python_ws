from typing import Final
def get_integer()->int :
    while True:
        num = input("Please enter an integer:")
        temp = num.strip()
        if temp[0] in ['+','-']:
            temp = temp[1::]
        if not temp.isdigit() :
            print("Incorrect value supplied!")
        else:
            return int(num)
        
def printTable(num : int)->None :
    TABLE_LIMIT :Final[int] = 11
    TABLE_START :Final[int] = 1
    if not isinstance(num,int):
        raise RuntimeError("The input to function sum_of_digits should be a integer ")
    for i in range (TABLE_START,TABLE_LIMIT):
        print(f'{num:^4d} X {i:^4d} = {(num*i):^4d}')
        
if __name__ == '__main__':
    num = get_integer()
    printTable(num)
        
