def get_primes(n: int):
    primes = [2]
    s = 2
    i = 3
    while i <= n:
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)
            primes.append(i)
            s += i
        i += 2
    return primes, s


print(get_primes(2e6))