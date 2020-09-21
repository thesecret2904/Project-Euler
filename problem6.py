sum1 = 0
sum2 = 0

limit = 100

for i in range(limit):
    sum1 += (i + 1) ** 2
    sum2 += i + 1

print(sum2 ** 2 - sum1)