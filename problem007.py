def get_primes(n: int):
    primes = [2]
    counter = 1
    i = 3
    while counter < n:
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            counter += 1
        i += 2
    return primes


print(get_primes(10001)[-1])
