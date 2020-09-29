# not solved
def triangle(n):
    return (n * (n + 1)) // 2


def square(n):
    return n * n


def pentagonal(n):
    return (n * (3 * n - 1)) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return (n * (5 * n - 3)) // 2


def octagonal(n):
    return n * (3 * n - 2)


def find(value: int, polygonal):
    right = 1
    left = 1
    while polygonal(right) < value:
        right *= 2
    while left <= right:
        middle = left + (right - left) // 2
        if polygonal(middle) == value:
            return middle
        else:
            if polygonal(middle) > value:
                right = middle - 1
            else:
                left = middle + 1
    return -1


def find_closest(value: int, polygonal):
    right = 1
    left = 1
    while polygonal(right) < value:
        right *= 2
    while left <= right:
        middle = left + (right - left) // 2
        if polygonal(middle) == value:
            return middle
        else:
            if polygonal(middle) > value:
                right = middle - 1
            else:
                left = middle + 1
    return left


possible_triangle = [(i, triangle(i)) for i in range(find_closest(1000, triangle), find_closest(10000, triangle))]
numbers = None
for index, number in possible_triangle:
    if number == 8256:
        print('here')
    remaining = [square, pentagonal, hexagonal, heptagonal, octagonal]
    numbers = [number]
    indices = [index]
    while len(remaining) > 0:
        current = numbers[-1]
        found = False
        for i in range(10, 100):
            to_check = int(str(current)[2:] + str(i))
            for poly in remaining:
                j = find(to_check, poly)
                if j > 0 and j not in indices:
                    numbers.append(to_check)
                    indices.append(j)
                    found = True
                    remaining.remove(poly)
                    break
            if found:
                break
        if not found:
            break
    if len(remaining) == 0 and str(numbers[-1])[2:] == str(numbers[0])[:2]:
        print(numbers, sum(numbers))
        break
