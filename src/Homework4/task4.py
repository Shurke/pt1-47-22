"""Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)"""


def degree_two(num):

    """Данная функция находит ближайшую степень двойки к
    числу поданному на вход."""

    control_num = num
    counter = 0
    while num > 1:
        num_1 = num / 2
        counter += 1
        num = round(num_1)
    num_2 = 2 ** counter
    return print(f"ближайшее число к числу {control_num} в "
                 f"степени 2 это \n{num_2}")


some_num = int(input("Введите число\n"))
degree_two(some_num)
