"""
Представьте, что сумма за пользование услугами такси складывается из базового тарифа в размере
4,00 BYN плюс 0,25 BYN за каждые 100 м поездки. Напишите функцию, принимающую в качестве
единственного параметра расстояние поездки в километрах и возвращающую итоговую сумму оплаты такси.
В основной программе должен демонстрироваться результат вызова функции.
"""


def cost_of_trip(trip_length=4.42) -> str:
    """Counts the cost of the trip"""
    import math
    num_of_points = math.ceil(trip_length * 10)
    start_cost = 4
    cost_per_100m = 0.25
    return f'Стоимость поездки: {(num_of_points * cost_per_100m) + start_cost} BYN'


if __name__ == '__main__':
    while True:
        trip = input('Пожалуйста, укажите протяжённость поездки в километрах (например, 4,299: ')
        try:
            print(cost_of_trip(float(trip.replace(',', '.'))))
        except ValueError:
            print('Пожалуйста, укажите число!')
