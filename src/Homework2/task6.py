"""Напишите программу, запрашивающую у пользователя целые числа,
пока он не оставит строку ввода пустой. После окончания ввода на
экран должны быть выведены сначала все отрицательные числа, которые
были введены, затем нулевые и только после этого положительные.
Внутри каждой группы числа должны отображаться в той последовательности,
в которой были введены пользователем.
Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2, вывод
должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1. Каждое значение должно
отображаться на новой строке."""

lis_pl = []
lis_min = []
lis_zero = []
lis1 = None
while True:
    lis1 = input("Введите число, или просто нажми Enter ")
    if lis1 == "":
        break
    elif int(lis1) > 0:
        lis_pl.append(lis1)
    elif int(lis1) < 0:
        lis_min.append(lis1)
    elif int(lis1) == 0:
        lis_zero.append(lis1)
new_lis = lis_min + lis_zero + lis_pl
print("Вы ввели следующие числа:")
for num in new_lis:
    print(num)
