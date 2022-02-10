""""
Вводится целое число. Вывести число, обратное введенному по порядку составляющих его цифр.
"""

a1 = int(input("Введите целое число: "))
a2 = 0

while a1 > 0:
    digit = a1 % 10
    a1 = a1 // 10
    a2 = a2 * 10
    a2 = a2 + digit
print('Обратное число:', a2)


"""
Дано число. Найти сумму и произведение его цифр.
"""

n = int(input("Введите число: "))
sum = 0
proizv = 1

while n > 0:
    digit = n % 10
    sum = sum + digit
    proizv = proizv * digit
    n = n // 10
print("Сумма:", sum)
print("Произведение:", proizv)


"""Рассчитать месячные выплаты (a) и суммарную выплату (b) по кредиту.
О кредите известно, что он составляет c рублей, берется на d лет, под e процентов.
"""

crd = input("Сколько  денег нужно: ")
crd = int(crd)
proc = input("Под какой процент: ")
proc = int(proc)
years = input("Насколько лет: ")
years = float(years)
proc = proc / 100
month_pay = (crd * proc * (1 + proc)**years) / (12 * ((1 + proc)**years - 1))
print("Сумма в месяц: %.2f" % month_pay)
summa = month_pay * years * 12
print("Сумма за всё время: %.2f" % summa)
