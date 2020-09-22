def get_sides(perimeter: int):
    possible = []
    for c in range(perimeter - 2, 0, -1):
        for b in range(perimeter - c - 1, 0, -1):
            a = perimeter - c - b
            if a ** 2 + b ** 2 == c ** 2:
                if (b, a, c) not in possible:
                    possible.append((a, b, c))
    return possible


max_p = 0
max_solutions = 0
for p in range(3, 1001):
    solutions = len(get_sides(p))
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p
print(max_p, max_solutions)
