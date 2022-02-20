"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

spis_in = list(input('Введите ряд чисел через пробел: ').split())
spis_par = []
for i in range(0, len(spis_in)):
    spis_par += [(int(spis_in[i]) + int(item_1)) / 2 for item_1 in spis_in[i + 1:]
                 if spis_in[i] == item_1]
spis_par2 = spis_par[:]
spis_uniqpar = list(set(spis_par2))
for i in range(0, len(spis_uniqpar)):
    print(f'Количество пар значений "{int(spis_uniqpar[i])}" составляет: '
          f'{spis_par2.count(spis_uniqpar[i])}')
