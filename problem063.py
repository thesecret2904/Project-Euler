from math import ceil


def get_bounds(n: int, root: int):
    lower_bound = ceil((10 ** (len(str(n)) - 1)) ** (1 / root))
    upper_bound = round((10 ** len(str(n))) ** (1 / root))
    return lower_bound, upper_bound


total = 0
for root in range(1, 200):
    l, u = get_bounds(10 ** (root - 1), root)
    total += u - l
print(total)
