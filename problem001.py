check_for = [3, 5]

bound = 1000

l = [i for i in range(min(check_for), bound) if min([i % j for j in check_for]) == 0]
print(l)
s = sum(l)

print(s)
