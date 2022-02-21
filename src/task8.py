""""
Вводится целое число. Вывести число, обратное введенному по порядку составляющих его цифр.
"""


CIF = int(input("Введите целое число: "))
NUM = 0

while CIF > 0:
    digit = CIF % 10
    CIF = CIF // 10
    NUM = NUM * 10
    NUM = NUM + digit
print('Обратное число:', NUM)


"""
Дано число. Найти сумму и произведение его цифр.
"""

n = int(input("Введите число: "))
SUM = 0
PI = 1

while n > 0:
    digit = n % 10
    SUM = PI + digit
    proizv = PI * digit
    n = n // 10
print("Сумма:", SUM)
print("Произведение:", PI)


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
print(f'Сумма выплат в месяц: {month_pay}')
summa = month_pay * years * 12
print(f'Сумма выплат за всё время: {summa}')


"""
Отсортируйте слова в алфавитном порядке
"""

STR = "Наш преподаватель работает  в крупной компании"
words = [word.lower() for word in STR.split()]
words.sort()

print("Полученные данные:")
for word in words:
    print(word)
