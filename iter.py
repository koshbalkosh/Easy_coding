Вводится список городов в одну строчку через пробел. 
Необходимо создать итератор для этого списка и с помощью итератора вывести на экран в столбик первые два значения (названия городов).


city = input().split()

it_city = iter(city)
print(next(it_city))
print(next(it_city))
