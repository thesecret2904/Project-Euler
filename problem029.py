a = range(2, 101)
b = range(2, 101)

terms = set()
for i in a:
    for j in b:
        terms.add(i ** j)
print(len(terms))