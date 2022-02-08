"""
5. Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и
условные операторы.
n - вводится
"""


n = int(input('Номер желаемого числа: '))
itter = 3
first_num = 0
second_num = 1
current_num = 0

while itter <= n:
    current_num = first_num + second_num
    first_num = second_num
    second_num = current_num
    itter += 1

print(f'Число, стоящее в ряду Фибоначчи под номером {itter-1}, это {current_num}.')
