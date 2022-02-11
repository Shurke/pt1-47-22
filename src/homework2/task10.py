"""
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка, не меняя
их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя, дополнительный
список использовать нельзя, задачу нужно выполнить за один проход по списку. Распечатайте полученный
список.
"""


LIST = [int(ELEM) for ELEM in input('Введите исходный список через пробел: ').split()]
AMOUNT_OF_NOT_ZERO = 0
AMOUNT_OF_ZERO = 0
while AMOUNT_OF_ZERO + AMOUNT_OF_NOT_ZERO != len(LIST):
    IND = AMOUNT_OF_ZERO + AMOUNT_OF_NOT_ZERO
    if LIST[IND] != 0:
        LIST.insert(AMOUNT_OF_NOT_ZERO, LIST.pop(IND))
        AMOUNT_OF_NOT_ZERO += 1
    else:
        AMOUNT_OF_ZERO += 1
print(LIST)
