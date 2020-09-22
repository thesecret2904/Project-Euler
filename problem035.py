def get_rotations(n):
    string = str(n)
    rotations = []
    for i in range(len(string)):
        s = ''
        for j in range(len(string)):
            s += string[(i + j) % len(string)]
        rotations.append(int(s))
    return rotations


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
            print(i)
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


primes = list(get_primes(10 ** 6))
circular = []
for p in primes:
    rotations = get_rotations(p)
    if sum([not is_prime(i, primes) for i in rotations]) == 0:
        circular.append(p)

print(len(circular))
