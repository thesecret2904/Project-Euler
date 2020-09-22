def is_pandigital(n):
    string = str(n)
    if len(string) == 9:
        return sum([str(i) not in string for i in range(1, 10)]) == 0
    else:
        return False


limit = 10 ** 6
pandigital_max = int(''.join([str(i * 9) for i in range(1, 6)]))
for i in range(10, limit):
    for j in range(2, 10):
        concatenated = int(''.join([str(i * k) for k in range(1, j)]))
        if is_pandigital(concatenated) and concatenated > pandigital_max:
            pandigital_max = concatenated
print(pandigital_max)
