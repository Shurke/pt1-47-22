"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для
каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка
начинается с названия страны, затем идут названия городов этой страны. В
следующей строке записано число M, далее идут M запросов — названия каких-то M
городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный
город.
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

number_of_countries = int(input("Введите количество стран: "))
dict_of_cities = {}
for i in range(0, number_of_countries):
    input_str_1 = input("Введите страну и города ч/з пробел: ")
    dict_of_cities[input_str_1.split()[0]] = input_str_1.split()[1:]

number_of_cities = int(input("Введите к-во городов, которые нужно найти: "))
output_list = []
for elem in range(0, number_of_cities):
    input_str_2 = input("Введите города: ")
    for key, value in dict_of_cities.items():
        if input_str_2 in value:
            output_list.append(key)

print("Ваши города находятся в этих странах: ")
for elem in output_list:
    print(elem)
