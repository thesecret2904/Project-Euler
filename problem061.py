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


def permutations(objects: list, all_permuations=[], current=[]):
    if len(current) == 0:
        for i in range(len(objects)):
            o = objects.copy()
            current = [o.pop(i)]
            permutations(o, all_permuations, current)
    elif len(objects) == 0:
        all_permuations.append(current)
    else:
        for i in range(len(objects)):
            o = objects.copy()
            c = current.copy()
            c.append(o.pop(i))
            permutations(o, all_permuations, c)
    return all_permuations


possible_triangle = [(i, triangle(i)) for i in range(find_closest(1000, triangle), find_closest(10000, triangle))]
numbers = None
possible_cycles = permutations([square, pentagonal, hexagonal, heptagonal, octagonal])

for index, number in possible_triangle:
    for cycle in possible_cycles:
        numbers = [number]
        indices = [index]
        for poly in cycle:
            current = numbers[-1]
            found = False
            for i in range(10, 100):
                to_check = int(str(current)[2:] + str(i))
                j = find(to_check, poly)
                if j > 0 and j not in indices:
                    numbers.append(to_check)
                    indices.append(j)
                    found = True
                    break
            if found:
                continue
            if not found:
                break
        if found:
            break
    if len(numbers) == len(possible_cycles[0]) + 1 and str(numbers[-1])[2:] == str(numbers[0])[:2]:
        print(numbers, sum(numbers))
        break
