"""
Двоичная пирамида.
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


def pyramid_bin(m, n):
    """string with the sum of the binary

    :param m: value 1 from user
    :param n: value 2 from user
    :return: sum of the binary
    """

    pyramid_sum = 0
    for elem in range(m, n + 1):
        pyramid_sum += int(str((bin(elem)))[2:])

    binary_sum = int(str(bin(pyramid_sum))[2:])
    return binary_sum


number_1 = int(input('Enter a number greater or equal to 0: '))
number_2 = int(input('Enter a number greater or equal to the previous number: '))
print(pyramid_bin(number_1, number_2))
