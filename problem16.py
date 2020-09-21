def sum_of_digits(num):
    string = str(num)
    numbers = [int(i) for i in string]
    return sum(numbers)


print(sum_of_digits(2 ** 1000))
