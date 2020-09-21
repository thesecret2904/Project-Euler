def fib():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


i = 1
for j in fib():
    if len(str(j)) > 999:
        break
    i += 1
print(i)
