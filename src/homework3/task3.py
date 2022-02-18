""" 3. Даны два списка чисел.
Посчитайте, сколько различных (встречаются только в одном из множеств)
чисел содержится одновременно как в первом списке, так и во втором.
"""


input_first = [int(x) for x in input("Введите элементы первого списка ч.з пробел: ").split()]
input_second = [int(x) for x in input("Введите элементы второго списка ч.з пробел: ").split()]

result = set(input_first).symmetric_difference(set(input_second))
print(f"списки содержат {len(result)} различных цифр: {result}")
