def digital_sum(n):
    return sum([int(i) for i in str(n)])


total = 0
for a in range(2, 100):
    for b in range(1, 100):
        s = digital_sum(a ** b)
        if s > total:
            total = s
print(total)
