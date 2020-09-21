# not solved
def read_pyramid(path):
    numbers = []
    with open(path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        row = [int(i) for i in line.split(' ')]
        numbers.append(row)
    return numbers


def evaluate_path(path):
    total = 0
    for i in range(0, len(path)):
        total += numbers[i][path[i]]
    return total


def is_valid(path):
    if path[0] != 0:
        return False
    for i in range(1, len(numbers)):
        if not (path[i] == path[i - 1] or path[i] == path[i - 1] + 1):
            return False
    return True


numbers = read_pyramid('problem18_2.txt')
path = [0]
for i in range(1, len(numbers)):
    if numbers[i][path[-1]] > numbers[i][path[-1] + 1]:
        path.append(path[-1])
    else:
        path.append(path[-1] + 1)

print(is_valid(path), evaluate_path(path))

print(len(numbers), len(numbers[-1]))
max_total = 0
for i in range(len(numbers)):
    total = numbers[-1][i] + numbers[0][0]
    current_col = i
    for j in range(len(numbers) - 2, 0, -1):
        if current_col == j + 1:
            current_col -= 1
        elif current_col > 0:
            if numbers[j][current_col] < numbers[j][current_col - 1]:
                current_col -= 1
        total += numbers[j][current_col]
    if total > max_total:
        max_total = total
print(max_total)