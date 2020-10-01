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


total = 0
for i in range(2, 10 ** 4):
    a, period = continued_fraction(i)
    print(a, period)
    if len(period) % 2 == 1:
        total += 1
print(total)
