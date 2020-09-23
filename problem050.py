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


limit = 10 ** 6
primes = list(get_primes(limit))
total_max = 0
terms = []
for i in range(0, len(primes)):
    for j in range(i + 1, len(primes) + 1):
        total = sum(primes[i:j])
        if total > limit:
            break
        if find(total) > -1 and j - i > len(terms):
            total_max = total
            terms = primes[i:j]
print(total_max, terms)
