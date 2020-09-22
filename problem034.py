limit = 10000000


def fac(n):
    prod = 1
    for i in range(1, n + 1):
       prod *= i
    return prod


factorials = []
for i in range(10, limit):
    digit_factorial_sum = sum([fac(int(c)) for c in str(i)])
    if digit_factorial_sum == i:
        factorials.append(i)

print(factorials)
print(sum(factorials))
