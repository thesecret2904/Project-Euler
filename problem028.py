import numpy as np


size = 1001

grid = np.zeros((size, size), dtype='uint')

start = size // 2
current = 1
pos = np.array((start, start))
move = np.array((0, 1))
max = size ** 2


def get_next(current):
    next = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
    return np.array(next[(current[0], current[1])])


while current <= max:
    grid[pos[0], pos[1]] = current
    if current == 1:
        pos += move
    else:
        new_move = get_next(move)
        new_pos = pos + new_move
        if grid[new_pos[0], new_pos[1]] == 0:
            pos = new_pos
            move = new_move
        else:
            pos += move

    current += 1
print(grid)
total = 0
for i in range(size):
    if i == size // 2:
        total += grid[i, i]
    else:
        total += grid[i, i] + grid[size - i - 1, i]
print(total)
