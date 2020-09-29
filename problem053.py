def fac(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def binomial(n, r):
    return fac(n) // (fac(r) * fac(n - r))


count = 0
for n in range(1, 101):
    # binomial coefficent of (n 0) and (n n) are always 1
    for r in range(1, n):
        if binomial(n, r) > 10 ** 6:
            count += 1
print(count)