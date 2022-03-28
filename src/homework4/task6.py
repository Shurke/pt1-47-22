"""
Представьте, что сумма за пользование услугами такси складывается из базового
тарифа в размере 4,00 BYN плюс 0,25 BYN за каждые 100 м поездки. Напишите
функцию, принимающую в качестве единственного параметра расстояние поездки в
километрах и возвращающую итоговую сумму оплаты такси. В основной программе
должен демонстрироваться результат вызова функции.
"""


def pay_taxi(distance):
    """Вычисляет сумму за пользование услугами такси, которая складывается из
    базового тарифа в размере 4,00 BYN плюс 0,25 BYN за каждые 100 м

    :param distance: Расстояние поездки
    :return: Итоговая сумма оплаты

    """
    res = 400 + 25 * distance * 10
    ruble = int(res // 100)
    penny = int(res % 100)
    return f"Плата за такси составляет {ruble} рублей, {penny} копеек"


input_number = float(input("Введите расстояние в км, например, 5 или 5.5: "))
print(pay_taxi(input_number))
