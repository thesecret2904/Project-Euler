with open('names.txt', 'r') as f:
    names = f.readline().replace("\"", "")

names = names.split(',')


def name_to_value(name):
    value = 0
    for i in range(len(name)):
        value += ord(name[i]) - 64
    return value


names.sort()
total = 0
for i in range(len(names)):
    total += name_to_value(names[i]) * (i + 1)
print(total)
