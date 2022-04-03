"""
Как ясно из названия, римские цифры появились еще в Древнем Риме. Но даже после падения Римской
империи они продолжали использоваться на территории Европы вплоть до позднего Средневековья, а в
определенных случаях применяются и сегодня.
Римские цифры базируются на обозначениях M, D, C, L, X, V и I, соответствующих числам 1000, 500,
100, 50, 10, 5 и 1.
'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
В основном римские цифры в составляющих их числах располагаются в порядке
убывания – от больших к меньшим. В этом случае итоговое число равно сумме всех составляющих его
римских цифр. Если цифры меньшего номинала предшествуют цифрам большего номинала, то первые
вычитаются из вторых и итог прибавляется к общей сумме. В такой манере могут использоваться римские
цифры C, X и I. При этом вычитание производится только из чисел, максимум в десять раз превосходящих
вычитаемое. Таким образом, цифра I может предшествовать V или X, но не может вычитаться из L, C, D
или M. А значит, число 99 должно быть написано как XCIX, а не IC.
Создайте рекурсивную функцию, которая будет переводить римскую запись чисел в десятичную. Функция
должна обрабатывать один или два символа в начале строки, после чего будет производиться ее
рекурсивный вызов для оставшихся символов. Используйте пустую строку с возвращаемым значением 0 в
качестве базового случая. Также напишите основную программу, которая будет запрашивать у
пользователя число, введенное римскими цифрами, и отображать его десятичный эквивалент. При этом
можно сделать допуск о том, что пользователь всегда вводит корректное число, так что обработку
ошибок вам реализовывать не нужно.

"""


def main():
    def get_arabian(roman_num: str) -> int:
        """Converts a Roman number to Arabic

        :param roman_num: input string with Roman number
        :return: Arabic number corresponding to a Roman number, or 0 if input not a Roman
        """
        numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        pairs = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        if len(roman_num) == 0:
            return 0
        if len(roman_num) == 1:
            return numbers[roman_num]
        elif roman_num[:2] in pairs:
            return pairs[roman_num[:2]] + get_arabian(roman_num[2:])
        else:
            return numbers[roman_num[0]] + get_arabian(roman_num[1:])

    while True:
        what_to_do = input('Please type Roman number, leave empty to demo or type exit: ')
        if what_to_do == 'exit':
            exit('Closed by user.')
        elif what_to_do != '':
            print(f'{what_to_do} = {get_arabian(what_to_do)}')
        else:
            for num in ['XCVII', 'CXLVIII', 'CLXXXVIII', 'MCMDCCXLIV']:
                print(f'{num} = {get_arabian(num)}')


if __name__ == '__main__':
    main()
