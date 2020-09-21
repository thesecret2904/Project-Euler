limit = 28123

abundant_numbers = [i for i in range(2, limit + 1) if sum([j for j in range(1, i) if i % j == 0]) > i]
possible = set()
for i in abundant_numbers:
    for j in abundant_numbers:
        possible.add(i + j)

print(possible)
not_possible = []
for i in range(1, limit):
    if i not in possible:
        not_possible.append(i)

print(sum(not_possible))
