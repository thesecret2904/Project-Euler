# not yet solved
def get_primes(n: int):
    with open('primes.txt', 'r') as f:
        p = 0
        while p <= n:
            try:
                p = int(f.readline())
                yield p
            except ValueError:
                break


def find(value: int):
    right = len(primes) - 1
    left = 0
    while left <= right:
        middle = left + (right - left) // 2
        if primes[middle] == value:
            return middle
        else:
            if primes[middle] > value:
                right = middle - 1
            else:
                left = middle + 1
    return -1


def permutations(objects: list, all_permuations=None, current=None, max_length=None):
    if max_length is None:
        max_length = len(objects)
    if current is None:
        all_permuations = []
        for i in range(len(objects)):
            o = objects.copy()
            current = [o.pop(i)]
            permutations(o, all_permuations, current, max_length)
    elif len(objects) == 0 or len(current) == max_length:
        all_permuations.append(current)
    else:
        for i in range(len(objects)):
            o = objects.copy()
            c = current.copy()
            c.append(o.pop(i))
            permutations(o, all_permuations, c, max_length)
    return all_permuations


limit = 10 ** 9
search_limit = 2 * 10 ** 2
primes = list(get_primes(limit))
for i in range(1, search_limit):
    for j in range(i + 1, search_limit):
        for k in range(j + 1, search_limit):
            for h in range(k + 1, search_limit):
                for l in range(h + 1, search_limit):
                    current = [primes[i], primes[j], primes[k], primes[h], primes[l]]
                    print(current)
                    if current == [3, 7, 109, 673]:
                        print('here')
                    combinations = permutations(current, max_length=2)
                    valid = True
                    for combination in combinations:
                        to_check = int(''.join([str(i) for i in combination]))
                        if find(to_check) < 0 or to_check > limit:
                            valid = False
                            break
                    if valid:
                        print(current, sum(current))
                        exit()
