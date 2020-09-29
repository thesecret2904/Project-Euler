def is_permutation(numbers: list):
    sets = [set([int(c) for c in str(i)]) for i in numbers]
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if sets[i] != sets[j]:
                return False
    return True


limit = 10 ** 6
count = 6
for i in range(1, limit):
    if is_permutation([i * j for j in range(1, count + 1)]):
        print([i * j for j in range(1, count + 1)])
        break
