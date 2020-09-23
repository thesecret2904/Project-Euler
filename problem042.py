def value(word: str):
    return sum([ord(c) - 64 for c in word])


def triangle_number(n: int):
    return (n * (n + 1)) // 2


def find(value: int):
    right = 1
    left = 1
    while triangle_number(right) < value:
        right *= 2
    while left <= right:
        middle = left + (right - left) // 2
        if triangle_number(middle) == value:
            return middle
        else:
            if triangle_number(middle) > value:
                right = middle - 1
            else:
                left = middle + 1
    return -1


with open('words.txt', 'r') as f:
    line = f.readline()

words = line.replace('\"', '').split(',')
print(len(words))
triangle_words = []

for w in words:
    i = find(value(w))
    if i < 0:
        print(i)
    else:
        triangle_words.append(w)

print(words)
print(len(words))
print(len(triangle_words))
