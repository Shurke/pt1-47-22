'''
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы
не знаем функции и рекурсию).
'''


NUM_1 = int(input('Введите первое число: '))
NUM_2 = int(input('Введите второе число: '))

LIST = [[NUM_1, NUM_2]]
while True:

    if LIST[0][0] == LIST[0][1]:
        print(f'НОД для этих чисел равен {LIST[0][0]}!')
        break
    else:
        MIN = min(LIST[-1][0], LIST[-1][1])
        MAX = max(LIST[-1][0], LIST[-1][1])
        NEW_LIST_ITEM = []
        NEW_LIST_ITEM.append(MAX - MIN)
        NEW_LIST_ITEM.append(MIN)
        LIST.clear()
        LIST.append(NEW_LIST_ITEM)
