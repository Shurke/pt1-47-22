"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
Входные данные: Программа получает на вход количество стран N. Далее идет N строк, каждая строка
начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то M городов,
перечисленных выше.
Выходные данные: Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры

Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa

3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""

CITY_DICT = {}
QUANT_COUNTRY = int(input('Введите количество стран: '))
for _ in range(QUANT_COUNTRY):
    country_city = input('Введите название страны и ее населенные пункты через пробел: ').split()
    CITY_DICT[country_city[0]] = country_city[1:]
print()                                             # readability
OUTPUT = []
QUANT_CITY = int(input('Введите количество городов: '))

for _ in range(QUANT_CITY):
    NAME_CITY = input('Введите название города: ')
    for country, city in CITY_DICT.items():
        if NAME_CITY in city:
            OUTPUT.append(country)
print()                                             # readability
print('Ваши города находятся в странах:')
for item in OUTPUT:
    print(item)
