def min_max(*number:int)->tuple:
    for item in number :
        if not (isinstance(item,int)):
            raise RuntimeError("Int is not passed to function min_max")
    if not number :
        return None,None
    minimum = min(number)
    maximum = max(number)
    return minimum,maximum

if __name__ == '__main__':
    minimum,maximum = min_max(4,5,3)
    print(f"minimum is {minimum} and maximum is {maximum}")