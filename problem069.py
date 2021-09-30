# from math import gcd
#
#
# def are_coprime(a, b):
#     return gcd(a, b) == 1
#
#
# def totient(n: int):
#     return 1 + len([i for i in range(2, n) if are_coprime(i, n)])
from math import sqrt


def get_primes(n: int):
    with open('primes.txt', 'r') as f:
        p = 0
        while p <= n:
            try:
                p = int(f.readline())
                yield p
            except ValueError:
                break


# Euler's product formula: https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula
def totient(n, primes):
    result = n
    if n in primes:
        return n - 1
    for p in primes:
        if p > n:
            return result
        else:
            if n % p == 0:
                result *= 1 - 1 / p
            while n % p == 0:
                n //= p
            if n == 1:
                return result


max_ratio = 1
max_n = 1
primes = list(get_primes(10 ** 6 + 1))
for i in range(2, 10 ** 6 + 1):
    t = totient(i, primes)
    print(i)
    ratio = i / t
    if ratio > max_ratio:
        max_ratio = ratio
        max_n = i
print(max_n)
