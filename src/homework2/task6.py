"""
Отрицательные, положительные и нули
Напишите программу, запрашивающую у пользователя целые числа, пока он не оставит строку ввода
пустой. После окончания ввода на экран должны быть выведены сначала все отрицательные числа, которые
были введены, затем нулевые и только после этого положительные. Внутри каждой группы числа должны
отображаться в той последовательности, в которой были введены пользователем.
Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2, вывод должен оказаться таким: -4,
-1, -2, 0, 0, 3 и 1. Каждое значение должно отображаться на новой строке.
"""


LIST_OF_NUMBERS = []
FLAG = True
while FLAG:
    ELEM = str(input('Введите следующее число последовательности: '))
    if ELEM != '':
        LIST_OF_NUMBERS.append(int(ELEM))
    else:
        FLAG = False

NEG_LIST = []
NULL_LIST = []
POS_LIST = []

for IND in range(0, len(LIST_OF_NUMBERS)):
    if LIST_OF_NUMBERS[IND] < 0:
        NEG_LIST.append(LIST_OF_NUMBERS[IND])
    elif LIST_OF_NUMBERS[IND] == 0:
        NULL_LIST.append(LIST_OF_NUMBERS[IND])
    else:
        POS_LIST.append(LIST_OF_NUMBERS[IND])

GEN_LIST = NEG_LIST + NULL_LIST + POS_LIST

for NUM in GEN_LIST:
    print(NUM)
