def permutations(objects: list, all_permuations=[], current=[]):
    if len(current) == 0:
        for i in range(len(objects)):
            o = objects.copy()
            current = [o.pop(i)]
            permutations(o, all_permuations, current)
    elif len(objects) == 0:
        all_permuations.append(current)
    else:
        for i in range(len(objects)):
            o = objects.copy()
            c = current.copy()
            c.append(o.pop(i))
            permutations(o, all_permuations, c)
    return all_permuations


# for magic 3-gon ring:
# groups = [(0, 1, 2), (3, 2, 4), (5, 4, 1)]
# for magic 5-gon ring
groups = [(0, 1, 2), (3, 2, 4), (5, 4, 6), (7, 6, 8), (9, 8, 1)]

possible = permutations(list(range(1, max([max(g) for g in groups]) + 2)))
solutions = 0
for set in possible:
    total = sum([set[i] for i in groups[0]])
    solution = True
    for i in range(1, len(groups)):
        if total != sum([set[j] for j in groups[i]]):
            solution = False
            break
    if solution:
        starting_min = 0
        for i in range(1, len(groups)):
            if set[groups[i][0]] < set[groups[starting_min][0]]:
                starting_min = i
        string = ''.join([''.join([str(set[i]) for i in groups[(i + starting_min) % len(groups)]]) for i in range(len(groups))])
        if int(string) > solutions and len(string) <= 16:
            solutions = int(string)
print(solutions)
