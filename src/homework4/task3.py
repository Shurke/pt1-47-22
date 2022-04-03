"""
Двоичная пирамида.
На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
Перевести числа от m до n (включительно) в двоичные числа.
Сложить полученные двоичные числа по основанию 10.
Перевести результат сложения в двоичную число.
Вернуть строку с результатом.
"""


def main():
    def binary_pyramid(m: int = 1, n: int = 4) -> str:
        """Return binary pyramid in range from /m/ to /n/"""
        pyramid_sum = 0

        for num in range(m, n + 1):
            pyramid_sum += int(str(bin(num))[2:])

        return str(bin(pyramid_sum))[2:]

    while True:
        what_to_do = input('Please type m & n separate by space or exit: ')
        if what_to_do == 'exit':
            exit('Closed by user')
        else:
            m__and_n = what_to_do.split()
            if len(m__and_n) == 2 and m__and_n[0].isdigit() and m__and_n[1].isdigit():
                m_int, n_int = int(m__and_n[0]), int(m__and_n[1])
                print(binary_pyramid(m_int, n_int))
            else:
                print('Incorrect data')


if __name__ == '__main__':
    main()
