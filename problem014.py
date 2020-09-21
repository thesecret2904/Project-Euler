def collatz(n):
    yield n
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n +1
        yield n

n = 1
length = 1

for i in range(2, int(1e6)):
    current = len([j for j in collatz(i)])
    if current > length:
        length = current
        n = i

print(n)
