"""
6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""


NUM = int(input('Число: '))
CHECK_SUM = 1
AMOUNT_OF_NUM = 1
CORRECT_CHECK = 0

while CHECK_SUM > 0:
    if NUM // (10 ** AMOUNT_OF_NUM):
        AMOUNT_OF_NUM += 1
    else:
        CHECK_SUM = 0

if AMOUNT_OF_NUM % 2 == 0:
    NUM_OF_CHECK = int(AMOUNT_OF_NUM / 2)
else:
    NUM_OF_CHECK = int((AMOUNT_OF_NUM - 1) / 2)

for CHECK in range(1, NUM_OF_CHECK + 1):
    LEFT = ((NUM // (10 ** (AMOUNT_OF_NUM - CHECK))) % 10)
    RIGHT = (NUM % (10 ** CHECK)) // (10 ** (CHECK - 1))

    if LEFT == RIGHT:
        CORRECT_CHECK += 1
    else:
        break

if CHECK == CORRECT_CHECK:
    print(f'Число {NUM} является полиндромом!')
else:
    print(f'Число {NUM} не является полиндромом!')
