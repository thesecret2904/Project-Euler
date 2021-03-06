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


def is_prime(n, primes):
    left = 0
    right = len(primes) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if primes[middle] == n:
            return True
        else:
            if primes[middle] > n:
                right = middle - 1
            else:
                left = middle + 1
    return False


def truncated(n):
    numbers = [n]
    string = str(n)
    for i in range(1, len(string)):
        numbers.append(int(string[i:]))
        numbers.append(int(string[:-i]))
    return numbers


primes = list(get_primes(10 ** 6))
truncatable = []
for p in primes:
    if p > 10:
        if sum([not is_prime(i, primes) for i in truncated(p)]) == 0:
            truncatable.append(p)
print(truncatable)
print(len(truncatable))
print(sum(truncatable))
