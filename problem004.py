def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


bound = 1000
palindromes = []
for i in range(bound - 1, 0, -1):
    for j in range(bound - 1, 0, -1):
        if is_palindrome(i * j):
            palindromes.append(i * j)
print(max(palindromes))
