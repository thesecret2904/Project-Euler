def get_primes(n: int):
    # first prime is 2
    yield 2
    primes = [2]
    # iterate over all odd number starting at 3
    i = 3
    while i <= n:
        is_prime = True
        # go over all current found prime numbers
        for j in primes:
            # if it is divisible by one prime number, current is not prime
            if i % j == 0:
                is_prime = False
                break
        # if current number is not divisible by any prime, it is prime
        if is_prime:
            primes.append(i)
            yield i
        i += 2


def find(value: int):
    right = len(primes) - 1
    left = 0
    while left <= right:
        middle = left + (right - left) // 2
        if primes[middle] == value:
            return middle
        else:
            if primes[middle] > value:
                right = middle - 1
            else:
                left = middle + 1
    return -1


def permutations(objects: list, all_permuations=None, current=None, max_length=None):
    if max_length is None:
        max_length = len(objects)
    if current is None:
        all_permuations = []
        for i in range(len(objects)):
            o = objects.copy()
            current = [o.pop(i)]
            permutations(o, all_permuations, current, max_length)
    elif len(objects) == 0 or len(current) == max_length:
        all_permuations.append(current)
    else:
        for i in range(len(objects)):
            o = objects.copy()
            c = current.copy()
            c.append(o.pop(i))
            permutations(o, all_permuations, c, max_length)
    return all_permuations


limit = 10 ** 6
target = 8
primes = list(get_primes(limit))

# iterate over all primes
for prime in primes:
    # get length of current prime and convert it to a string
    string = str(prime)
    length = len(string)
    # replace l digits in the current prime
    for l in range(1, length):
        # get every possible combinations
        positions = permutations(list(range(length)), max_length=l)
        # go over all possible combinations
        for pos in positions:
            # keep track of all found primes
            current_primes = []
            # replace all positions with the same digit 'i'
            for i in range(10):
                new_string = string
                # skip it if you would put a zero in front of the number
                if i == 0 and 0 in pos:
                    continue
                # replace j-th digit with 'i'
                for j in pos:
                    new_string = new_string[:j] + f'{i}' + new_string[j + 1:]
                # if the new obtained number is a prime append it to the list of primes
                if find(int(new_string)) > -1:
                    current_primes.append(new_string)
            # if enough primes were found, print them and terminate the program
            if len(current_primes) >= target:
                print(current_primes)
                exit()
