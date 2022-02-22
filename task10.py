"""
Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка, не меняя их порядок,
а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""

print("Введите список элементов через пробел")
main_list = [int(i) for i in input().split()]
for i in reversed(range(len(main_list))):
    if main_list[i] == 0:
        main_list.append(main_list.pop(i))
print(main_list)

