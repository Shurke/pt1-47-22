"""Написать программу которая находит ближайшую степень двойки к введенному числу. 10(8), 20(16),
 1(1), 13(16)
"""


number = int(input('Введиче число для нахождения ближайшей степени двойки: '))
last_result = 1


while number >= 2**last_result:
    previous = last_result
    last_result += 1

if number == 1:
    print('Ближайшую степень двойки к введенному числу', number)
elif number - (2**previous) > (2**last_result) - number:
    print('Ближайшую степень двойки к введенному числу', (2**last_result))
else:
    print('Ближайшую степень двойки к введенному числу', (2**previous))
