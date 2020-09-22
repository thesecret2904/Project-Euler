def get_digits():
    current = 1
    current_string = str(current)
    while True:
        if len(current_string) > 0:
            yield int(current_string[0])
            current_string = current_string[1:]
        else:
            current += 1
            current_string = str(current)


count = 0
limit = 20
positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
digits = []
for i in get_digits():
    count += 1
    if count in positions:
        digits.append(i)
    if count == positions[-1]:
        break
print(digits)
prod = 1
for i in digits:
    prod *= i
print(prod)
