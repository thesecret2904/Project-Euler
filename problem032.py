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


pandigital = set()
for p in permutations(list(range(1, 10))):
    a = int(str(p[0]) + str(p[1]))
    b = int(str(p[2]) + str(p[3]) + str(p[4]))
    c = int(str(p[5]) + str(p[6]) + str(p[7]) + str(p[8]))
    if a * b == c:
        pandigital.add(c)
    a = int(str(p[0]))
    b = int(str(p[2]) + str(p[3]) + str(p[4]) + str(p[1]))
    c = int(str(p[5]) + str(p[6]) + str(p[7]) + str(p[8]))
    if a * b == c:
        pandigital.add(c)
print(pandigital, len(pandigital))
print(sum(pandigital))
