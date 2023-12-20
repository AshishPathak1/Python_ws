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
        
def check_if_palindrome(num :int)->bool:
    if not isinstance(num,int):
        raise RuntimeError("The input to function check_if_palindrome should be a integer ")
    import math
    reversed_num = 0
    temp = int(math.fabs(num))
    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp = temp // 10
    else :
        return reversed_num == int(math.fabs(num)) 
       
        
if __name__ == '__main__':
    num = get_integer()
    print(f"{num} is a palindrome ? {check_if_palindrome(num)}")