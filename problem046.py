from math import sqrt


def get_primes(n: int):
    # first prime is 2
    yield 2
    primes = [2]
    # iterate over all odd number starting at 3
    i = 3
    while i <= n:
        is_prime = True
        # go over all current found prime numbers
        for j in primes:
            # if it is divisible by one prime number, current is not prime
            if i % j == 0:
                is_prime = False
                break
        # if current number is not divisible by any prime, it is prime
        if is_prime:
            primes.append(i)
            yield i
        i += 2


def goldbach(n):
    for p in primes:
        if p > n:
            raise ValueError
        square = round(sqrt((n - p) // 2))
        if n == p + 2 * square ** 2:
            return p, square


def find(value: int):
    right = len(primes) - 1
    left = 0
    while left <= right:
        middle = left + (right - left) // 2
        if primes[middle] == value:
            return middle
        else:
            if primes[middle] > value:
                right = middle - 1
            else:
                left = middle + 1
    return -1


limit = 10 ** 5
primes = list(get_primes(limit))
for i in range(3, limit, 2):
    if find(i) < 0:
        try:
            goldbach(i)
        except ValueError:
            print(i)
            exit()
