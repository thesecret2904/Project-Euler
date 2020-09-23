def pentagon_number(n):
    return (n * (3 * n - 1)) // 2


def find(value: int):
    right = 1
    left = 1
    while pentagon_number(right) < value:
        right *= 2
    while left <= right:
        middle = left + (right - left) // 2
        if pentagon_number(middle) == value:
            return middle
        else:
            if pentagon_number(middle) > value:
                right = middle - 1
            else:
                left = middle + 1
    return -1


pair = (0, 0)
difference = None

limit = 5000
for i in range(1, limit):
    for j in range(i + 1, limit):
        p = pentagon_number(i)
        q = pentagon_number(j)
        # note: q > p because j > i
        if find(p + q) > 0 and find(q - p) > 0:
            d = q - p
            print(p, q, d)
            if difference is None:
                difference = d
                pair = (i, j)
            elif d < difference:
                difference = d
                pair = (i, j)
print(difference)
