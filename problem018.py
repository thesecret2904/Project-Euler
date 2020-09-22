import random
from math import exp


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


def fix_path(path):
    path[0] = 0
    for i in range(1, len(numbers)):
        if path[i] < path[i - 1]:
            path[i] = path[i - 1]
        elif path[i] > path[i - 1] + 1:
            path[i] = path[i - 1] + 1
    return path


def simulated_annealing(init: list, cost: callable, t: float = 15., dt: float = 1e-5, k: float = 2.5):
    # save initial as best
    current_best = init.copy()
    current_best_cost = cost(init)
    current = init
    current_cost = current_best_cost
    # as long as the 'temperature' is positive do
    while t > 0:
        # change the current path in one position
        new = current.copy()
        random_index = random.randint(1, len(new) - 1)
        if new[random_index] == new[random_index - 1]:
            new[random_index] += 1
        else:
            new[random_index] -= 1
        # fix the path as is it may get invalid
        new = fix_path(new)

        # evaluate the new value
        new_cost = cost(new)
        # if new value is better set it as current
        if new_cost > current_cost:
            current = new
            current_cost = current_best_cost
            # if it is better than the current best, save it as current best
            if new_cost > current_best_cost:
                current_best_cost = new_cost
                current_best = new
        # if new value is worse still take it with a random chance
        if random.random() < exp((new_cost - current_cost) / (k * t)):
            current = new
            current_cost = new_cost
        t -= dt
    return current_best


numbers = read_pyramid('problem018_2.txt')
# generate random (valid) path
path = [0]
for i in range(1, len(numbers)):
    path.append(path[-1] + random.randint(0, 1))

print(is_valid(path), evaluate_path(path))
# optimize path with simulated annealing
path = simulated_annealing(path, evaluate_path)
print(is_valid(path), evaluate_path(path))
