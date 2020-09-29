def SieveOfEratosthenes(limit: int):
    prime = [True if i == 2 or i % 2 == 1 else False for i in range(limit + 1)]
    print('Init of Array complete!')
    p = 3
    while p * p <= limit:
        if prime[p]:
            for i in range(p * 2, limit + 1, p):
                prime[i] = False
        p += 2
        print(p)
    print('Complete with loop!\nNow saving every prime!')
    prime[0] = False
    prime[1] = False
    for p in range(limit + 1):
        if prime[p]:
            yield p


if __name__ == '__main__':
    limit = 10 ** 9
    with open('primes.txt', 'w+') as f:
        for p in SieveOfEratosthenes(limit):
            f.write(f'{p}\n')

