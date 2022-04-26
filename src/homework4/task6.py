"""
Плата за такси. Представьте, что сумма за пользование услугами такси складывается из базового
тарифа в размере 4,00 BYN плюс 0,25 BYN за каждые 100 м поездки.
Напишите функцию, принимающую в качестве единственного параметра расстояние поездки в километрах и
возвращающую итоговую сумму оплаты такси.
В основной программе должен демонстрироваться результат вызова функции.
"""


def tax_cost(distance):
    """trip cost calculation

    :param distance: distance from user
    :return: cost ride
    """
    basic_rate = 4
    distance_rate = 0.25
    cost = basic_rate + distance_rate * 10 * distance

    return f'The cost of your trip is {cost} BYN'


distance_trip = float(input('Enter the distance in km: '))
print(tax_cost(distance_trip))
