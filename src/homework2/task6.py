"""
Напишите программу, запрашивающую у пользователя целые числа, пока
он не оставит строку ввода пустой. После окончания ввода на экран
должны быть выведены сначала все отрицательные числа, которые были
введены, затем нулевые и только после этого положительные. Внутри
каждой группы числа должны отображаться в той последовательности,
в которой были введены пользователем.
Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2,
вывод должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1. Каждое
значение должно отображаться на новой строке.
"""

list_input = []
while True:
    str_input = str(input("Введите число: "))
    if str_input == "":
        break
    else:
        list_input.append(int(str_input))
negative_list = []
zero_list = []
positive_list = []
for item in list_input:
    if item < 0:
        negative_list.append(item)
    elif item == 0:
        zero_list.append(item)
    else:
        positive_list.append(item)
result_list = negative_list + zero_list + positive_list
for elem in result_list:
    print(elem)
