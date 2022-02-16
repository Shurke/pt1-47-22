"""
Для выигрыша главного приза необходимо, чтобы шесть номеров на
лотерейном билете совпали с шестью числами, выпавшими случайным
образом в диапазоне от 1 до 49 во время очередного тиража.
Напишите программу, которая будет случайным образом подбирать
шесть номеров для вашего билета. Убедитесь в том, что среди этих чисел
не будет дубликатов. Выведите номера билетов на экран по возрастанию.
"""

import random

number = [int(s) for s in input("Введите 6 номеров через пробел: ").split()]
list1 = []
while len(list1) < 6:
    number2 = random.randint(1, 49)
    if number2 not in list1:
        list1.append(number2)
print(sorted(list1))
print(sorted(number))
if list1 == number:
    print("Вы выиграли!")
else:
    print("В следующий раз повезёт!")
