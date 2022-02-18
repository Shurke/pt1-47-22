'''
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в
какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с
названия страны, затем идут названия городов этой страны. В следующей строке записано число M, далее
идут M запросов — названия каких-то M городов, перечисленных выше.

Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
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
'''


DICT_OF_CITIES = {}

NUM_OF_COUNTRIES = int(input('Введите количество стран: '))
for i in range(0, NUM_OF_COUNTRIES):
    START_INPUT = input('Страна и города: ')
    DICT_OF_CITIES[START_INPUT.split()[0]] = START_INPUT.split()[1:]
OUTPUT = []

NUM_OF_CITIES = int(input('Сколько город хотите вывести?\n'))
for CHAR in range(0, NUM_OF_CITIES):
    FINAL_INPUT = input('Какой город вас интересует?\n')
    for COUNTRY, CITIES in DICT_OF_CITIES.items():
        if FINAL_INPUT in CITIES:
            OUTPUT.append(COUNTRY)

print('\nВаши города в этих странах (порядок сохранён):')

for CHAR in OUTPUT:
    print(CHAR)
