""""
Вводится целое число. Вывести число, обратное введенному по порядку составляющих его цифр.
"""

cif = int(input("Введите целое число: "))
num = 0

while cif > 0:
    digit = cif % 10
    cif = cif // 10
    num = num * 10
    num = num + digit
print('Обратное число:', num)

"""
Дано число. Найти сумму и произведение его цифр.
"""

n = int(input("Введите число: "))
summ = 0
piec = 1

while n > 0:
    digit = n % 10
    summ = piec + digit
    proizv = piec * digit
    n = n // 10
print("Сумма:", summ)
print("Произведение:", piec)

"""
Рассчитать месячные выплаты (a) и суммарную выплату (b) по кредиту.
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
