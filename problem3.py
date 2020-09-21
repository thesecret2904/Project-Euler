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


def prime_factors(n: int):
    # list of all current prime factors
    primes = []
    # loop over all primes up to n
    for p in get_primes(n):
        # if current prime is a prime factor append it to the list
        if n % p == 0:
            primes.append(p)
            # check if all prime factors have been found
            prod = 1
            for i in primes:
                prod *= i
            if prod == n:
                # if all have been found exit function
                break
    return primes


print(prime_factors(13195))
factors = prime_factors(600851475143)
print(factors[-1])
