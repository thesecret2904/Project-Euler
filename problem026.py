def decimal(d):
    cycle = []
    mods = []
    current = 10
    while True:
        div = current // d
        current = (current % d) * 10
        try:
            i = mods.index(current)
            return cycle[:i], cycle[i:]
        except ValueError:
            pass
        cycle.append(div)
        mods.append(current)
        if current == 0:
            return cycle, []


max_length = 0
max_d = 2
for i in range(2, 1000):
    pre, cycle = decimal(i)
    if len(cycle) > max_length:
        max_length = len(cycle)
        max_d = i
        print(i, cycle)

print(max_d)
