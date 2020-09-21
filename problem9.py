from math import sqrt


def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def get_triplets(bound):
    triplets = []
    for i in range(1, bound + 1):
        for j in range(1, i):
            k = round(sqrt(i ** 2 + j ** 2))
            if is_pythagorean_triplet(i, j, k):
                triplets.append((i, j, k))
    return triplets


triplets = get_triplets(1000)

for triplet in triplets:
    if sum(triplet) == 1000:
        print(triplet, triplet[0] * triplet[1] * triplet[2])