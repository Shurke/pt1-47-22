"""
Как ясно из названия, римские цифры появились еще в Древнем Риме. Но даже после
падения Римской империи они продолжали использоваться на территории Европы
вплоть до позднего Средневековья, а в определенных случаях применяются и сегодня.
Римские цифры базируются на обозначениях M, D, C, L, X, V и I, соответствующих
числам 1000, 500, 100, 50, 10, 5 и 1. В основном римские цифры в составляющих
их числах располагаются в порядке убывания – от больших к меньшим. В этом случае
итоговое число равно сумме всех составляющих его римских цифр. Если цифры
меньшего номинала предшествуют цифрам большего номинала, то первые вычитаются из
вторых и итог прибавляется к общей сумме. В такой манере могут использоваться
римские цифры C, X и I. При этом вычитание производится только из чисел,
максимум в десять раз превосходящих вычитаемое. Таким образом, цифра I может
предшествовать V или X, но не может вычитаться из L, C, D или M. А значит, число
99 должно быть написано как XCIX, а не IC.
Создайте рекурсивную функцию, которая будет переводить римскую запись чисел в
десятичную. Функция должна обрабатывать один или два символа в начале строки,
после чего будет производиться ее рекурсивный вызов для оставшихся символов.
Используйте пустую строку с возвращаемым значением 0 в качестве базового случая.
Также напишите основную программу, которая будет запрашивать у пользователя
число, введенное римскими цифрами, и отображать его десятичный эквивалент. При
этом можно сделать допуск о том, что пользователь всегда вводит корректное
число, так что обработку ошибок вам реализовывать не нужно.
"""


def get_translate(number_roman):
    """Преобразовывает число, введенное римскими цифрами, в десятичный эквивалент

    :param number_roman: Число, введенное римскими цифрами
    :return: Число в десятичной системе счисления

    """

    dict_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                  "M": 1000}

    number_decimal = 0
    i = 0
    if len(number_roman) == 1:
        number_decimal += dict_value[number_roman[0]]
        return number_decimal
    if dict_value[number_roman[0]] >= dict_value[number_roman[1]]:
        number_decimal += dict_value[number_roman[0]]
    else:
        number_decimal -= dict_value[number_roman[0]]
    i += 1
    return number_decimal + get_translate(number_roman[i:])


if __name__ == "__main__":
    number_roman_input = input("Введите число римскими цифрами: ")
    print(get_translate(number_roman_input))
