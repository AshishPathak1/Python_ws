from math import factorial

def get_integer()->int:
    while True:
        try:
            num = eval(input("Enter a Number :"))
            if not isinstance(num, int):
                raise TypeError
            if num < 0:
                raise ValueError("The Number has to be a whole number!")
        except (TypeError, NameError) :
            print("Specify the Number in Numeric format only as integer")
        except ValueError as err:
            print(f"Error Message :{err}")
        # except SyntaxError:
        #     num = int(num)
        else:
            return num

if __name__ == '__main__':
    num = get_integer()
    print(f'The factorial of {num} is {factorial(num)}')
#issue is with leading zeroes of input integer
#limit is of 43 digits for any answer