"""Вводится число найти его максимальный делитель, являющийся
степенью двойки. 10(2) 16(16), 12(4)."""


def nod_of_two(num):

    """Данная функция находит максимальный делитель
    числа подоного на вход который является степенью двойки."""

    control_num = num
    counter = 0
    while True:
        if num % 2 == 0:
            counter += 1
            num = num / 2
        else:
            break
    digital = 2 ** counter
    return print(f"для числа \n{control_num} \nмаксимальный "
                 f"делитель являющийся степенью двойки "
                 f"являетcя \n{digital}")


num_1 = int(input("Введите ваше число\n"))
nod_of_two(num_1)
