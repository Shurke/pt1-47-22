"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка
начинается с названия страны, затем идут названия городов этой страны. В следующей
строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
"""


data_count = int(input('Введите количество стран: '))
data_lst = []
for i in range(data_count):
    input_data = input('Введите страну затем города через пробел: ').split(' ')
    data_lst.append(input_data)

city_count = int(input('Введите количество запрашеваемых городов: '))
cities_request = []
for request in range(city_count):
    input_cities = input('Введите название города: ')
    cities_request.append(input_cities)

data = {
    data_lst[country][city]: data_lst[country][0]
    for country in range(len(data_lst)) for city in range(1, len(data_lst[country]))
}

for city in cities_request:
    print(f'Город {city} находится в стране {data[city]}')
