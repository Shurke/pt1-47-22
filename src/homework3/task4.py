""" 4. Даны два списка чисел.
Посчитайте, сколько различных чисел входит только в один из этих списков
(например, есть в первом списке, но нет во втором).
"""


input_first = [int(x) for x in input("Введите элементы первого списка ч.з пробел: ").split()]
input_second = [int(x) for x in input("Введите элементы второго списка ч.з пробел: ").split()]

result1 = set(input_first).difference(set(input_second))
result2 = set(input_second).difference(set(input_first))
print(
    f"первый список содержит {len(result1)} цифр которые не входят во второй: {result1}\n"
    f"второй список содержит {len(result2)} цифр которые не входят в первый: {result2}"
)
