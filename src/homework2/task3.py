"""
Tuple practice
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу последовательно
выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
"""


TUPLE = str(123),
for CHAR in TUPLE[0]:
    print(CHAR)
print(len(TUPLE))

# OR

TUPLE = [1, 2, 3],
for CHAR in TUPLE[0]:
    print(CHAR)
print(len(TUPLE))
