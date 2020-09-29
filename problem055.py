def is_palindrom(n: int):
    s = str(n)
    return s == s[::-1]


def reverse(n):
    return int(str(n)[::-1])


def is_lychrel(n):
    for i in range(50):
        n += reverse(n)
        if is_palindrom(n):
            return False
    return True


print(sum((is_lychrel(i) for i in range(10 ** 4))))
