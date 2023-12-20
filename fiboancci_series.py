# 0,1,1,2,3,5,8,13

def fibonacci(num1:int)->int:
    a =[0,1]
    for i in range(2,num+1):
        a.append(a[i-1]+a[i-2])
    return a[num-1]

def fibonacci_rec(num:int,a=[0,1])->int:
    if len(a) < num:
        a.append(a[-1] + a[-2])
        return fibonacci_rec(num,a)
    return a[num-1]

if __name__ == "__main__":
    num = int(input("Enter an integer:"))
    ans = fibonacci_rec(num)
    print(f"{num}th number is {ans}")