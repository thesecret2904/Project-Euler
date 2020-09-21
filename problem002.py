def fibonacci_numbers(limit):
    a = 1
    b = 2
    yield a
    yield b
    while b < limit:
        a, b = b, a + b
        yield b

list = [i for i in fibonacci_numbers(4e6) if i % 2 == 0]

print(sum(list))
