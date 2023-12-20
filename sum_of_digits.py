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
    

def sum_of_digits(num :int)->int :
    if not isinstance(num,int):
        raise RuntimeError("The input to function sum_of_digits should be a integer ")
    
    import math
    digit_sum = 0
    temp = int(math.fabs(num))
    while temp != 0:
        digit = temp % 10
        digit_sum = digit_sum + digit
        temp = temp // 10
    else:
        return digit_sum

if __name__ == '__main__':
    num = get_integer()
    digit_sum = sum_of_digits(num)
    print(f'The sum of digits of {num} is {digit_sum}')
#    digit_sum = sum_of_digits("123")