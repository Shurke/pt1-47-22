"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

numbers = tuple(int(nmbr) for nmbr in input('Введите числа через пробел: ').split())
couples = 0
for char in range(0, len(numbers)):
    for char2 in range(char + 1, len(numbers)):
        if numbers[char] == numbers[char2]:
            couples += 1
print(f'Количество пар в строке: {couples}')
