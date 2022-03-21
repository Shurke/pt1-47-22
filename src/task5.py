"""Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16),
 12(4).
"""


number = int(input('Введите число: '))

list_exp = [i**2 for i in range(1, (number + 1)) if i**2 <= number]
for i in range(number, -1, -1):
    if number % i == 0:
        if list_exp.count(i) == 1:
            break
print(f'Максимальный делитель введенного числа являющийся степенью двойки: {i}')
