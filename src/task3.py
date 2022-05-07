"""Двоичная пирамида.
На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
Перевести числа от m до n (включительно) в двоичные числа.
Сложить полученные двоичные числа по основанию 10.
Перевести результат сложения в двоичную число.
Вернуть строку с результатом.

Пример:
func(1, 4)   -->  1111010
    1  // 1 в двоичном виде 1
+  10  // 2 в двоичном виде 10
+  11  // 3 в двоичном виде 11
+ 100  // 4 в двоичном виде 100
-----
  122  // 122 в двоичном виде 1111010
"""


def func_1(number_to_binary):
    """Функция переводит входящее число в  двоичное"""
    string_of_numbers = ''
    while number_to_binary > 0:
        string_of_numbers = str(number_to_binary % 2) + string_of_numbers
        number_to_binary = number_to_binary // 2
    return string_of_numbers


def func(number_1, number_2):
    """Функция передает числа из интервала полученных чисел на перевод в двоичне и складывает
    полученные результаты

    :nnumber_1: начало интервала
    :number_2: Конец интервала
    """
    result = int()
    for i in range(number_1, number_2 + 1):
        number_to_binary = func_1(i)
        print(f'{i} в двоичном коде {number_to_binary}')
        result += int(number_to_binary)
    return result


NUMBERS = func(1, 4)
NUMBER_RESULT = func_1(NUMBERS)
print(f'{NUMBERS} в двоичном коде {NUMBER_RESULT}')
