# not yet solved simple brute-force takes to long
from math import gcd


def are_coprime(a, b):
    return gcd(a, b) == 1


def totient(n: int):
    return 1 + len([i for i in range(2, n) if are_coprime(i, n)])


max_ratio = 1
max_n = 1
for i in range(2, 10 ** 6 + 1):
    print(i)
    ratio = i / totient(i)
    if ratio > max_ratio:
        max_ratio = ratio
        max_n = i
print(max_n)
