import sys
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return a


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


def square_root(n, start=None):
    if n == 1:
        total = (1, 2)
    else:
        total = div(1, add(2, square_root(n - 1, 0)))
    if start is None:
        return add(1, total)
    else:
        return total


total = 0
sys.setrecursionlimit(1005)
for i in range(1, 1001):
    expansion = square_root(i)
    if len(str(expansion[0])) > len(str(expansion[1])):
        total += 1
print(total)
