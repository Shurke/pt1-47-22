"""
Двоичная пирамида.
На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
Перевести числа от m до n (включительно) в двоичные числа.
Сложить полученные двоичные числа по основанию 10.
Перевести результат сложения в двоичную число.
Вернуть строку с результатом.
"""


def binary_pyramid(m=1, n=4) -> str:
    """Return binary pyramid in range from /m/ to /n/"""
    pyramid_sum = 0

    for num in range(m, n + 1):
        pyramid_sum += int(str(bin(num))[2:])

    return str(bin(pyramid_sum))[2:]


if __name__ == '__main__':
    while True:
        what_to_do = input('Please type m & n separate by space or exit: ')

        if what_to_do == 'exit':
            exit('Closed by user')

        else:
            try:
                m__and_n = what_to_do.split()
                m_int, n_int = int(m__and_n[0]), int(m__and_n[1])
                print(binary_pyramid(m_int, n_int))
            except IndexError:
                print('Too little data')
