# for mathematics see: https://de.wikipedia.org/wiki/Pellsche_Gleichung
from math import sqrt, gcd


def continued_fraction(n: int):
    a0 = int(sqrt(n))
    if a0 * a0 == n:
        return a0, []
    i, j, k = 1, a0, 1
    a = int((i * k * sqrt(n) + j * k) // (i * i * n - j * j))
    period = [a]
    i, j, k = i * k, -j * k + a * (i * i * n - j * j), i * i * n - j * j
    divisor = gcd(i, gcd(j, k))
    i //= divisor
    j //= divisor
    k //= divisor
    coefficents = [(i, j, k)]
    while True:
        a = int((i * k * sqrt(n) + j * k) // (i * i * n - j * j))
        i, j, k = i * k, -j * k + a * (i * i * n - j * j), i * i * n - j * j
        divisor = gcd(i, gcd(j, k))
        i //= divisor
        j //= divisor
        k //= divisor
        if (i, j, k) == coefficents[0]:
            break
        period.append(a)
        coefficents.append((i, j, k))
    return a0, period


def reduce(a, b):
    g = gcd(a, b)
    return a // g, b // g


def add(f1, f2):
    if type(f1) == int:
        f1 = (f1, 1)
    if type(f2) == int:
        f2 = (f2, 1)
    return reduce(f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1])


def div(f1, f2):
    if type(f1) == int:
        f1 = (f1, 1)
    if type(f2) == int:
        f2 = (f2, 1)
    return reduce(f1[0] * f2[1], f1[1] * f2[0])


def continued_fraction_to_fraction(a: int, terms: list):
    if len(terms) == 0:
        return a
    total = (1, terms[-1])
    for i in range(len(terms) - 2, -1, -1):
        total = div(1, add(terms[i], total))
    return add(a, total)


def get_sol(D: int):
    a0, period = continued_fraction(D)
    if len(period) == 0:
        raise ValueError('D must not be a square number!')
    if len(period) % 2 == 0:
        return continued_fraction_to_fraction(a0, period[:-1])
    else:
        period *= 2
        return continued_fraction_to_fraction(a0, period[:-1])


max_x = 0
max_D = 0
for i in range(2, 1001):
    try:
        x, y = get_sol(i)
        if x > max_x:
            max_x = x
            max_D = i
    except ValueError:
        pass
print(max_D)
