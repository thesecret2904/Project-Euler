list = []
for i in range(2, 10000):
    list.append((i, sum([j for j in range(1, i) if i % j == 0])))

amicable_numbers = set()
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i][1] == list[j][0] and list[i][0] == list[j][1]:
            amicable_numbers.add(list[i][0])
            amicable_numbers.add(list[j][0])
            print(list[i][0], list[j][0])

print(sum(amicable_numbers))
