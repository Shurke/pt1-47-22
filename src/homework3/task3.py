"""
Даны два списка чисел. Посчитайте, сколько различных (встречаются только в
одном из множеств) чисел содержится одновременно как в первом списке, так и
во втором.
"""

str_1 = input("Введите 1 список ч/з пробел: ").split()
set_1 = set(str_1)
str_2 = input("Введите 2 список ч/з пробел: ").split()
set_2 = set(str_2)
set_new = set_1 ^ set_2
print(f"{len(set_new)} различных чисел содержится в двух списках")
