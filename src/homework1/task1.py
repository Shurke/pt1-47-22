"""
Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара.
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""
import re


def get_total_price(cost, quantity):
    """Считает общую цену за количество товаров

    :param str cost: цена за единицу в формате xx.yy или xx,yy
    :param int quantity: количество товаров
    :returns: кортеж с общей стоимостью (руб.коп)
    :rtype: tuple
    """
    rub, kop = [int(x) for x in re.split('[,.]', cost)]
    rub = rub * quantity + ((kop * quantity) // 100)
    kop = (kop * quantity) % 100
    return (rub, kop)


C = input("Введите цену (руб.коп): ")
Q = int(input("Введите количество товаров: "))
r = get_total_price(C, Q)
print(f"Общая цена {r[0]} рублей {r[1]} копеек")
