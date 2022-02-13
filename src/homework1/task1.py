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


input_cost = input("Введите цену (руб.коп): ")
input_quantity = int(input("Введите количество товаров: "))
result = get_total_price(input_cost, input_quantity)
print(f"Общая цена {result[0]} рублей {result[1]} копеек")
