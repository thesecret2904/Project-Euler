def permutations(objects: list, all_permuations=None, current=None):
    if current is None:
        all_permuations = []
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


pandigitals = permutations(list(range(10)))
divisors = [2, 3, 5, 7, 11, 13, 17]
numbers = []
for i in pandigitals:
    string = ''.join([str(n) for n in i])
    if sum([int(string[j + 1:j + 4]) % divisors[j] != 0 for j in range(len(divisors))]) == 0:
        numbers.append(int(string))

print(numbers)
print(sum(numbers))

