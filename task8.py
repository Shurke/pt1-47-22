"""
Подмножеством элементов, или подсписком (sublist), мы будем называть список, являющийся составной частью большего списка.
Подсписок может содержать один элемент, множество элементов, а также быть пустым.
Например, [1], [2], [3] и [4] являются подсписками списка [1, 2, 3, 4].
Список [2, 3] также входит в состав [1, 2, 3, 4], но при этом список [2, 4] не является подсписком [1, 2, 3, 4], поскольку в исходном списке числа 2 и 4 не соседствуют друг с другом.
Пустой список может быть рассмотрен как подсписок для любого списка.
Таким образом, список [] является под- списком [1, 2, 3, 4].
Также список является подсписком самого себя, то есть [1, 2, 3, 4] – это подсписок для [1, 2, 3, 4]. В рамках данного упражнения вам необходимо написать программу, определяющую, является ли один список подсписком другого. На вход должны поступать два списка – larger и smaller.
Программа должна возвращать значение True только в том случае, если список smaller является подсписком списка larger.
"""

print("Введите элементы большого массива через пробел")
larger_list = [i for i in input().split()]
print("Введите элементы маленького массива через пробел")
smaller_list = [i for i in input().split()]
sublists = [[]]
for i in range(len(larger_list) + 1):
    for j in range(i):
        sublists.append(larger_list[j: i])
if smaller_list in sublists:
    print(True)
else:
    print(False)

