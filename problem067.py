def read_pyramid(path):
    numbers = []
    with open(path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        row = [int(i) for i in line.split(' ')]
        numbers.append(row)
    return numbers


def evaluate_path(path: list):
    return sum([numbers[i][path[i]] for i in range(len(path))])


# def get_best(current_path: list = None, current_best: list = None):
#     if current_path is None:
#         current_path = [0]
#         current_best = current_path
#     if len(current_path) == len(numbers):
#         return current_path
#     if evaluate_path(current_path) > evaluate_path(current_best):
#         current_best = current_path
#     if evaluate_path(current_path) + sum(
#             [max(numbers[i][current_path[-1]:]) for i in range(len(current_path), len(numbers))]) > evaluate_path(
#             current_best):
#         path1 = get_best(current_path.copy() + [current_path[-1]], current_best)
#         if evaluate_path(path1) > evaluate_path(current_best):
#             current_best = path1
#         path2 = get_best(current_path.copy() + [current_path[-1] + 1], current_best)
#         return path1 if evaluate_path(path1) > evaluate_path(path2) else path2
#     return current_path


def get_best(numbers: list):
    for i in range(len(numbers) - 2, -1, -1):
        for j in range(len(numbers[i])):
            numbers[i][j] += max(numbers[i + 1][j], numbers[i + 1][j + 1])
    return numbers[0][0]


numbers = read_pyramid('p067_triangle.txt')
print(get_best(numbers))
