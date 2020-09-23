def triangle(n):
    return (n * (n + 1)) // 2


def pentagonal(n):
    return (n * (3 * n - 1)) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def find_pent(value: int):
    right = 1
    left = 1
    while pentagonal(right) < value:
        right *= 2
    while left <= right:
        middle = left + (right - left) // 2
        if pentagonal(middle) == value:
            return middle
        else:
            if pentagonal(middle) > value:
                right = middle - 1
            else:
                left = middle + 1
    return -1


def find_hex(value: int):
    right = 1
    left = 1
    while hexagonal(right) < value:
        right *= 2
    while left <= right:
        middle = left + (right - left) // 2
        if hexagonal(middle) == value:
            return middle
        else:
            if hexagonal(middle) > value:
                right = middle - 1
            else:
                left = middle + 1
    return -1


i = 286
while find_hex(triangle(i)) < 0 or find_pent(triangle(i)) < 0:
    i += 1
print(i, triangle(i))
