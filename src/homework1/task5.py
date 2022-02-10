"""
5. Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и
условные операторы.
n - вводится
"""


N = int(input('Номер желаемого числа: '))
ITTER = 3
FIRST_NUM = 0
SECOND_NUM = 1
CURRENT_NUM = 0

while ITTER <= N:
    CURRENT_NUM = FIRST_NUM + SECOND_NUM
    FIRST_NUM = SECOND_NUM
    SECOND_NUM = CURRENT_NUM
    ITTER += 1

print(f'Число, стоящее в ряду Фибоначчи под номером {ITTER - 1}, это {CURRENT_NUM}.')
