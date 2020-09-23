def get_primes(n: int):
    # first prime is 2
    yield 2
    primes = [2]
    # iterate over all odd number starting at 3
    i = 3
    while i <= n:
        is_prime = True
        # go over all current found prime numbers
        for j in primes:
            # if it is divisible by one prime number, current is not prime
            if i % j == 0:
                is_prime = False
                break
        # if current number is not divisible by any prime, it is prime
        if is_prime:
            primes.append(i)
            yield i
        i += 2


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


def is_permutation(numbers: list):
    sets = [set([int(c) for c in str(i)]) for i in numbers]
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if sets[i] != sets[j]:
                return False
    return True


limit = 10 ** 4
primes = list(get_primes(limit))
start = 10 ** 3
i = 0
while primes[i] < start:
    i += 1
for j in range(i, len(primes)):
    for k in range(j + 1, len(primes)):
        if is_permutation([primes[j], primes[k]]):
            to_check = 2 * primes[k] - primes[j]
            if find(to_check) > 0 and is_permutation([primes[j], to_check]):
                print(primes[j], primes[k], to_check, sep='')
