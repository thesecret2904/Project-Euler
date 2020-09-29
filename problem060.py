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


def check_pair(a, b):
    p1 = int(str(a) + str(b))
    p2 = int(str(b) + str(a))
    if find(p1) < 0:
        return False
    if find(p2) < 0:
        return False
    return True


limit = 10 ** 9
search_limit = 10 ** 4
primes = list(get_primes(limit))
for i in range(1, search_limit):
    for j in range(i + 1, search_limit):
        if not check_pair(primes[i], primes[j]):
            continue
        for k in range(j + 1, search_limit):
            if not check_pair(primes[i], primes[k]):
                continue
            if not check_pair(primes[j], primes[k]):
                continue
            for h in range(k + 1, search_limit):
                if not check_pair(primes[i], primes[h]):
                    continue
                if not check_pair(primes[j], primes[h]):
                    continue
                if not check_pair(primes[k], primes[h]):
                    continue
                for l in range(h + 1, search_limit):
                    if not check_pair(primes[i], primes[l]):
                        continue
                    if not check_pair(primes[j], primes[l]):
                        continue
                    if not check_pair(primes[k], primes[l]):
                        continue
                    if not check_pair(primes[h], primes[l]):
                        continue
                    print(primes[i], primes[j], primes[k], primes[h], primes[l])
                    print(sum([primes[i], primes[j], primes[k], primes[h], primes[l]]))

