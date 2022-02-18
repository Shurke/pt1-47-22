"""
6. Отрицательные, положительные и нули
Напишите программу, запрашивающую у пользователя целые числа,
пока он не оставит строку ввода пустой. После окончания ввода на
экран должны быть выведены сначала все отрицательные числа,
которые были введены, затем нулевые и только после этого
положительные. Внутри каждой группы числа должны отображаться
в той последовательности, в которой были введены пользователем.
Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2, вывод
должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1. Каждое значение должно
отображаться на новой строке.
"""


number_list = []
negative_numbers = []
zero_numbers = []
positive_numbers = []

while True:
    number = input('Введите целое число. Для оканчания ввода оставьте строку пустой: ')
    if number != '':
        number_list.append(int(number))
    else:
        break

for i in number_list:
    if i < 0:
        negative_numbers.append(i)
    elif i == 0:
        zero_numbers.append(i)
    elif i > 0:
        positive_numbers.append(i)

number_list = sorted(negative_numbers) + zero_numbers + sorted(positive_numbers)
print('Отсортированный список', number_list)
