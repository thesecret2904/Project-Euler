from math import isclose


def common_digit(a, b):
    str_a = str(a)
    str_b = str(b)
    common = []
    for c in str_a:
        if c in str_b:
            common.append(int(c))
    return common


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return a


fractions = []
for i in range(11, 100):
    for j in range(i + 1, 100):
        common = common_digit(i, j)
        if 0 in common:
            continue
        elif len(common) > 0:
            new_i = int(str(i).replace(str(common[0]), '', 1))
            new_j = int(str(j).replace(str(common[0]), '', 1))
            try:
                if isclose(i / j, new_i / new_j):
                    fractions.append((i, j))
            except ZeroDivisionError:
                pass
print(fractions)
a, b = 1, 1
for f in fractions:
    a *= f[0]
    b *= f[1]
print(a, b)
g = gcd(a, b)
print(a // g, b // g)
