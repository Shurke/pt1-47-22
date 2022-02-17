"""
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""


input_list = [int(elmt) for elmt in input('Введите числа через пробел: ').split()]
summ_nmbr = 0
null_summ = 0
while null_summ + summ_nmbr != len(input_list):
    total = null_summ + summ_nmbr
    if input_list[total] != 0:
        input_list.insert(summ_nmbr, input_list.pop(total))
        summ_nmbr += 1
    else:
        null_summ += 1
print(f'Упорядоченный список {input_list}')
