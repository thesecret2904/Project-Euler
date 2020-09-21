limit = 10000000

numbers = []
for i in range(2, limit):
    if i == sum([int(c) ** 5 for c in str(i)]):
        numbers.append(i)
print(numbers)
print(sum(numbers))