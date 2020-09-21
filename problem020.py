def fac(n):
    prod = 1
    for i in range(1, n):
        prod *= i
    return prod


def sum_of_digits(n):
    return sum([int(i) for i in str(n)])


print(sum_of_digits(fac(100)))
