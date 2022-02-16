"""
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается,
что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

list1 = [int(elem) for elem in input("Введите список через пробел: ").split()]
sum1 = 0
for item1 in range(len(list1)):
    for item2 in range(item1 + 1, len(list1)):
        if list1[item1] == list1[item2]:
            sum1 += 1
print(f"Количество пар {sum1}")
