"""
6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково). Число положительное
целое, произвольной длины. Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
"""


num = int(input('Число: '))
check_sum = 1
amount_of_num = 1
correct_check = 0

while check_sum > 0:
    if num // (10 ** amount_of_num):
        amount_of_num += 1
    else:
        check_sum = 0

if amount_of_num % 2 == 0:
    num_of_check = int(amount_of_num/2)
else:
    num_of_check = int((amount_of_num - 1) / 2)

for check in range(1, num_of_check + 1):
    left = ((num // (10**(amount_of_num - check))) % 10)
    right = (num % (10**check)) // (10**(check - 1))

    if left == right:
        correct_check += 1
    else:
        break

if check == correct_check:
    print(f'Число {num} является полиндромом!')
else:
    print(f'Число {num} не является полиндромом!')
