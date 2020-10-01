# not yet solved
from math import sqrt


def get_y(x: int, D: int):
    if round(sqrt(D)) ** 2 == D:
        raise ValueError('D must not be a square number!')
    y = round(sqrt((x * x - 1) / D))
    return x * x - D * y * y == 1, y


def get_x(y: int, D: int):
    if round(sqrt(D)) ** 2 == D:
        raise ValueError('D must not be a square number!')
    x = round(sqrt(1 + D * y * y))
    return x * x - D * y * y == 1, x


def get_minimal_solution(D: int):
    x = round(sqrt(1 + D))
    try:
        sol, y = get_y(x, D)
    except ValueError:
        return None, None
    last = 'y'
    while not sol:
        if last == 'y':
            y += 1
            sol, x = get_x(y, D)
            last = 'x'
        else:
            x += 1
            sol, y = get_y(x, D)
            last = 'y'
        if D == 61:
            print(x, y)
    return x, y


max_x = get_minimal_solution(2)[0]
max_D = 2
for i in range(2, 10 ** 3 + 1):
    print(i)
    x, y = get_minimal_solution(i)
    print(x, y)
    if x is not None:
        if x > max_x:
            max_x = x
            max_D = i
print(max_D)
