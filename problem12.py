from math import sqrt, floor


def get_triangle_numbers():
    n = 2
    while True:
        s = 0
        for i in range(1, n):
            s += i
        n += 1
        yield s


def get_divisors(n):
    divisors = []
    for i in range(1, floor(sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return divisors

count = 0
limit = 500
gen = get_triangle_numbers()
while count <= limit:
    current = next(gen)
    count = len(get_divisors(current))

print(current)
