n = int(input("Enter the numberber of prime numberbers you want: "))

prime_number = []
number = 2

while len(prime_number) < n:
    is_prime = True
    for prime in prime_number:
        if number % prime == 0:
            is_prime = False
            break
    if is_prime:
        prime_number.append(number)
        print(number)
    number += 1
