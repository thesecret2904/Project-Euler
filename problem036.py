def is_palindrom(string: str):
    return string == string[-1::-1]


palindromic = []
for i in range(1, 10 ** 6):
    if is_palindrom(str(i)) and is_palindrom(str(bin(i))[2:]):
        palindromic.append(i)
print(sum(palindromic))
