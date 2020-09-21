def get_number_of_days(month, year):
    number_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 1:
        return number_of_days[month]
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28


weekday, day, month, year = 0, 1, 0, 1900

while (day, month, year) != (1, 0, 1901):
    weekday = (weekday + 1) % 7
    day += 1
    if day > get_number_of_days(month, year):
        day, month = 1, month + 1
        if month == 12:
            year += 1
            month = 0

print(weekday, day, month, year)
total = 0
while (day, month, year) != (31, 11, 2000):
    weekday = (weekday + 1) % 7
    day += 1
    if day > get_number_of_days(month, year):
        day, month = 1, month + 1
        if month == 12:
            year += 1
            month = 0
    if weekday == 6 and day == 1:
        total += 1
print(total)
