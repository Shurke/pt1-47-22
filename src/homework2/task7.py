""" 7. Случайные лотерейные номера
Для выигрыша главного приза необходимо, чтобы шесть номеров на лотерейном билете совпали
с шестью числами, выпавшими случайным образом в диапазоне от 1 до 49 во время очередного тиража.
Напишите программу, которая будет случайным образом подбирать шесть номеров для вашего билета.
Убедитесь в том, что среди этих чисел не будет дубликатов.
Выведите номера билетов на экран по возрастанию.
"""
import random


def get_random_lottery_tickets(number):
    """Возвращает сгенерированые лотерейные билеты

    :param int number: количество билетов которые необходимо сгенерировать и вернуть
    :returns: список элементов с номерами сгенерированных билетов
    :rtype: list
    """
    result = list()
    while len(result) < number:
        while True:
            t = get_random_ticket_id()
            if t not in result:
                result.append(t)
                break
    return result


def get_random_ticket_id():
    """Возвращает номера сгенерированного билета

    :returns: кортеж элементов с номерами в билете
    :rtype: tuple
    """
    result = list()
    while len(result) < 6:
        while True:
            temp_n = random.randint(1, 49)
            if temp_n not in result:
                result.append(temp_n)
                break
    return tuple(result)


TICKETS_NUM_INPUT = int(input("Введите необходимое количество билетов: "))
TICKETS_LST = get_random_lottery_tickets(TICKETS_NUM_INPUT)
TICKETS_LST.sort()
for ticket in TICKETS_LST:
    print(" ".join([str(x) for x in ticket]))
