with open('problem13.txt', 'r') as f:
    lines = f.readlines()


numbers = []
for line in lines:
    numbers.append(int(line))

s = sum(numbers)
print(str(s)[:10])
