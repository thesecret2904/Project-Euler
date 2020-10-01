from math import e, gcd


def continued_fraction(MAX_DEPTH: int):
    a0 = int(e)
    if MAX_DEPTH == 1:
        return a0, []
    period = []
    k = 1
    for i in range(MAX_DEPTH - 1):
        if i % 3 == 1:
            period.append(2 * k)
            k += 1
        else:
            period.append(1)
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


print(continued_fraction(100))
print(continued_fraction_to_fraction(*continued_fraction(100)))
print(sum([int(c) for c in str(continued_fraction_to_fraction(*continued_fraction(100))[0])]))
