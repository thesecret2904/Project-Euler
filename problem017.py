def number_to_word(num):
    basics = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
              10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
              17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
              60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 0: ''}

    if num <= 20:
        return basics[num]

    # check for 1000
    if num == 1000:
        return 'one thousand'
    string = ''
    # check for numbers > 99
    hundred = num // 100
    num %= 100
    if hundred > 0:
        string += f'{basics[hundred]} hundred'
        if num == 0:
            return string
        else:
            string += ' and '
    if num > 20:
        ten = (num // 10) * 10
        num %= 10
        string += basics[ten]
        if num > 0:
            string += f'-{basics[num]}'
    else:
        string += basics[num]
    return string

print(len(number_to_word(115).replace(' ', '').replace('-', '')))

limit = 1000
letters = 0
for i in range(1, limit + 1):
    print(i, number_to_word(i))
    letters += len(number_to_word(i).replace(' ', '').replace('-', ''))
print(letters)
