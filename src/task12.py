"""Римские цифры
Как ясно из названия, римские цифры появились еще в Древнем Риме. Но даже после падения Римской
империи они продолжали использоваться на территории Европы вплоть до позднего Средневековья, а в
определенных случаях применяются и сегодня.
Римские цифры базируются на обозначениях M, D, C, L, X, V и I, соответствующих числам 1000, 500,
100, 50, 10, 5 и 1. В основном римские цифры в составляющих их числах располагаются в порядке
убывания – от больших к меньшим. В этом случае итоговое число равно сумме всех составляющих его
римских цифр. Если цифры меньшего номинала предшествуют цифрам большего номинала, то первые
вычитаются из вторых и итог прибавляется к общей сумме. В такой манере могут использоваться римские
цифры C, X и I. При этом вычитание производится только из чисел, максимум в десять раз
превосходящих вычитаемое. Таким образом, цифра I может предшествовать V или X, но не может
вычитаться из L, C, D или M. А значит, число 99 должно быть написано как XCIX, а не IC.
Создайте рекурсивную функцию, которая будет переводить римскую запись чисел в десятичную. Функция
должна обрабатывать один или два символа в начале строки, после чего будет производиться ее
рекурсивный вызов для оставшихся символов. Используйте пустую строку с возвращаемым значением 0 в
качестве базового случая. Также напишите основную программу, которая будет запрашивать у
пользователя число, введенное римскими цифрами, и отображать его десятичный эквивалент. При этом
можно сделать допуск о том, что пользователь всегда вводит корректное число, так что обработку
ошибок вам реализовывать не нужно.
"""


def roman_numer(number):
    """Функция переводит римские цифры в десятичные"""
    roman_numeral = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    if number in roman_numeral:
        return roman_numeral[number]
    first, second = map(roman_numer, number[:2])
    if first < second:
        return second - first + roman_numer(number[2:])
    else:
        return first + roman_numer(number[1:])


if __name__ == '__main__':
    roman_input = input('Введите римскую цифру которую хотите конвертировать: ')
    print(f'{roman_input} в десятичной системе исчисления будет: {roman_numer(roman_input)}')
