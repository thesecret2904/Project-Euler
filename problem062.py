from math import ceil


def is_permutation(a: int, b: int):
    a = [int(c) for c in str(a)]
    b = [int(c) for c in str(b)]
    a.sort()
    b.sort()
    return a == b


def get_bounds(n: int):
    lower_bound = ceil((10 ** (len(str(n)) - 1)) ** (1 / 3))
    upper_bound = ceil((10 ** len(str(n))) ** (1 / 3))
    return lower_bound, upper_bound


limit = 10 ** 6
count = 5
for i in range(1, limit):
    n = i ** 3
    l, u = get_bounds(n)
    numbers = [n]
    bases = [i]
    for j in range(l, u):
        if i != j:
            if is_permutation(n, j ** 3):
                numbers.append(j ** 3)
                bases.append(j)
    if len(numbers) >= count:
        print(numbers)
        print(bases)
        break
