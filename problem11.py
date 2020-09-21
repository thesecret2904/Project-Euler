with open('problem11.txt', 'r') as f:
    lines = f.readlines()

grid = []
for line in lines:
    row = []
    numbers = line[:-1].split(' ')
    for n in numbers:
        row.append(int(n))
    grid.append(row)

count = 4

factors = None
positions = []
product = 0

for i in range(len(grid)):
    for j in range(len(grid)):
        # check vertically
        if i + count - 1 < len(grid):
            current_factors = []
            pos = []
            prod = 1
            for k in range(count):
                current_factors.append(grid[i + k][j])
                pos.append((i + k, j))
                prod *= grid[i + k][j]
                if prod > product:
                    product = prod
                    positions = pos
                    factors = current_factors
        # check horizontally
        if j + count - 1 < len(grid):
            current_factors = []
            pos = []
            prod = 1
            for k in range(count):
                current_factors.append(grid[i][j + k])
                pos.append((i, j + k))
                prod *= grid[i][j + k]
                if prod > product:
                    product = prod
                    positions = pos
                    factors = current_factors
        # check diagonally
        if i + count - 1 < len(grid) and j + count - 1 < len(grid):
            current_factors = []
            pos = []
            prod = 1
            for k in range(count):
                current_factors.append(grid[i + k][j + k])
                pos.append((i + k, j + k))
                prod *= grid[i + k][j + k]
                if prod > product:
                    product = prod
                    positions = pos
                    factors = current_factors
        if i + count - 1 < len(grid) and j - count + 1 >= 0:
            current_factors = []
            pos = []
            prod = 1
            for k in range(count):
                current_factors.append(grid[i + k][j - k])
                pos.append((i + k, j - k))
                prod *= grid[i + k][j - k]
                if prod > product:
                    product = prod
                    positions = pos
                    factors = current_factors

print(factors, product, positions)
