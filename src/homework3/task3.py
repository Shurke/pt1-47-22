"""
Даны два списка чисел. Посчитайте, сколько различных (встречаются только в одном из множеств)
чисел содержится одновременно как в первом списке, так и во втором.
"""
FIRST_LIST = (input("Введите числа разделяя пробелом для первого списка"))
SECOND_LIST = (input("Введите числа разделяя пробелом для второго списка"))
count_sum = 0
count_sum_1 = 0
for i in FIRST_LIST:
    if i not in SECOND_LIST:
        count_sum += 1
for s in SECOND_LIST:
    if s not in FIRST_LIST:
        count_sum_1 += 1
print("Кол-во различий между списками: ", count_sum + count_sum_1)
