from math import ceil, sqrt


def permutations(objects: list, all_permuations=None, current=None):
    if current is None:
        all_permuations = []
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


def list_to_int(l: list):
    return int(''.join([str(i) for i in l]))


def is_prime(n: int):
    if n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


pandigital_numbers = []
for i in range(2, 10):
    p = permutations(list(range(1, i + 1)))
    for l in p:
        pandigital_numbers.append(list_to_int(l))

pandigital_numbers.sort()
pandigital_numbers.reverse()

for i in pandigital_numbers:
    if is_prime(i):
        print(i)
        break
