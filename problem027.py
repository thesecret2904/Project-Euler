from math import sqrt, ceil


def is_prime(n):
    if n <= 0:
        return False
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def number_of_primes(a, b):
    def f(n):
        return n ** 2 + a * n + b
    n = 0
    while is_prime(f(n)):
        n += 1
    return n


max_a, max_b = 0, 0
current_max = number_of_primes(0, 0)
for a in range(1, 1000):
    for b in range(1, 1000):
        current = number_of_primes(a, b)
        if current > current_max:
            current_max = current
            max_a, max_b = a, b
        current = number_of_primes(a, -b)
        if current > current_max:
            current_max = current
            max_a, max_b = a, -b
        current = number_of_primes(-a, b)
        if current > current_max:
            current_max = current
            max_a, max_b = -a, b
        current = number_of_primes(-a, -b)
        if current > current_max:
            current_max = current
            max_a, max_b = -a, -b
print(max_a * max_b)
