"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с
названия страны, затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
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
"""


dict_of_countries = {}
count_of_countries = int(input('Введите количество стран: '))
list_of_countries = []
print('Введите сначала страну, затем города этой страны.')

for i in range(0, count_of_countries):
    request = input('Страна и города: ').split()
    dict_of_countries[request[0]] = request[1:]

numb = int(input('Введите какое количество городов вас интересует: '))
print('Далее введите города и получите страны, в которых эти города находяться')

for i in range(0, numb):
    city = input('Введите город: ')
    for k, v in dict_of_countries.items():
        if city in v:
            list_of_countries.append(k)

print('Список стран интересующих городов:')

for char in list_of_countries:
    print(char)
