"""
4. Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных
друг другу. Считается, что любые два элемента, равные друг другу
образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


string = input('Введите строку, разделённую пробелами: ')
list1 = sorted(string.split())
res_list = []
pairs = []
i = 0

for char in list1:
    if char not in res_list:
        res_list.append(char)
        value = list1.count(char)
        pair = (value * (value - 1)) / 2
        pairs.append(int(pair))

while i < len(res_list):
    print(f'Число {res_list[i]} содержит {pairs[i]} пар')
    i += 1
