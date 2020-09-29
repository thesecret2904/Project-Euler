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


limit = 10 ** 9
primes = list(get_primes(limit))

current_size = 1
current = 1
ratio = 1
total = 1
total_primes = 0
while current < limit and ratio > 0.1:
    current_size += 2
    for i in range(4):
        current += current_size - 1
        if find(current) > -1:
            total_primes += 1
        total += 1
    ratio = total_primes / total
    print(current_size, ratio)
