# Вывести на экран календарь заданного месяца года

import calendar

year = int(input('Введите год: '))
month = int(input('Введите месяц: '))

print(calendar.month(year, month))
