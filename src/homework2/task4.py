"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

TUPLE = tuple(int(ELEM) for ELEM in input('Введите последовательность через пробел: ').split())
NUM_OF_PAIRS = 0
for I_CHAR in range(0, len(TUPLE)):
    for I_CHAR_1 in range(I_CHAR + 1, len(TUPLE)):
        if TUPLE[I_CHAR] == TUPLE[I_CHAR_1]:
            NUM_OF_PAIRS += 1
print(NUM_OF_PAIRS)
