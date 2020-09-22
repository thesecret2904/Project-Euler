value = 200
base = [1, 2, 5, 10, 20, 50, 100, 200]
max_values = [200 // i for i in base]

current = [0] * len(base)
current[1] = -1
possible_combinations = 0

while current[-1] < max_values[-1]:
    # only permutate 2 pence and larger
    for i in range(1, len(base)):
        current[i] += 1
        if current[i] > max_values[i]:
            if i < len(base) - 1:
                current[i] = 0
        else:
            break
    total = sum([base[i] * current[i] for i in range(1, len(base))])
    # if the total value is less than the target, it can be filled (uniquely) with one pence coins
    if total <= value:
        possible_combinations += 1
print(possible_combinations)
