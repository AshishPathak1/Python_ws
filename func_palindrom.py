def get_integer()->int :
    while True:
        num = input("Please enter an integer:")
        temp = num.strip()
        if temp[0] in ['+','-']:
            temp = temp[1::]
        if not temp.isdigit() :
            print("Incorrect value supplied!")
            continue
        else:
            num = int(num)
            break
    return num

def check_palindrom(num :int)->bool:
    if not(isinstance(num,int)):
        raise RuntimeError("The input to function check_palindrom should be a integer ")
    num_str = str(num)
    return num_str == num_str[::-1]

if __name__ == '__main__':
    num = get_integer()
    print(f"{num} is a palindrome ? {check_palindrom(num)}")
