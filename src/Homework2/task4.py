"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую
необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар"""

lis = input("Введите числа списка разделеные пробелами\n")
new_lis = lis.split()
new_lis.sort()
lis_num = []
lis_long = []
number = 0
for num in new_lis:
    if num not in lis_num:
        lis_num.append(num)
        count = new_lis.count(num)
        long = (count * (count - 1)) / 2
        lis_long.append(int(long))
while number < len(lis_num):
    print("Число ", lis_num[number], "имеет ", lis_long[number], "пар")
    number += 1
