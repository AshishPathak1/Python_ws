def min_max(*number)->tuple:
    minimum = min(number)
    maximum = max(number)
    return minimum,maximum

if __name__ == '__main__':
    # wish = True
    # number = ()
    # while wish == True :
    #     num = int(input('Enter an integer '))
    #     number = number + (num,)
    #     wish = input('Do you want to continue ? (Y/N)')
    #     if wish.upper() == 'Y' :
    #         wish == True
    #     else :
    #         wish == False
    minimum,maximum = min_max(7,6,5,2,1,3)
    print(f"minimum is {minimum} and maximum is {maximum}")

    minimum,maximum = min_max()
    print(f"minimum is {minimum} and maximum is {maximum}")