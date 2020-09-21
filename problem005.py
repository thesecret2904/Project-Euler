numbers = list(range(1, 21))

m = max(numbers)
i = numbers[-1] + m
while True:
    cond = True
    for j in numbers:
        if i % j != 0:
            cond = False
            break
    if cond:
        print(i)
        break
    i += m
