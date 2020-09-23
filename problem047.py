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


def get_prime_factors(n, max_factors):
    prime_factors = []
    count = []
    while n > 1:
        for p in primes:
            if n % p == 0:
                n //= p
                try:
                    i = prime_factors.index(p)
                    count[i] += 1
                except ValueError:
                    prime_factors.append(p)
                    count.append(1)
                    if len(prime_factors) > max_factors:
                        n = 1
    return [prime_factors[i] ** count[i] for i in range(len(count))]


def distinct(factors: list):
    for i in range(len(factors)):
        for j in range(i + 1, len(factors)):
            for factor in factors[i]:
                if factor in factors[j]:
                    return False
    return True


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
count = 4
factors = []
for i in range(10 ** 5, limit):
    print(i)
    to_check = [j for j in range(i, i + count)]
    if len(factors) == 0:
        factors = [get_prime_factors(j, count) for j in to_check]
    else:
        factors = factors[1:]
        factors.append(get_prime_factors(to_check[-1], count))
    if sum([len(l) != count for l in factors]) == 0:
        if distinct(factors):
            print(to_check)
            break
# print(*factors, sep='\n')
