"""Написать программу которая находит ближайшую степень двойки к введенному числу. 10(8), 20(16),
 1(1), 13(16)
"""


number = int(input('Введиче число для нахождения ближайшей степени двойки: '))
LAST_RESULT = 1


while number >= 2**LAST_RESULT:
    PREVIOUS = LAST_RESULT
    LAST_RESULT += 1

if number == 1:
    print('Ближайшую степень двойки к введенному числу', number)
elif number - (2 ** PREVIOUS) > (2 ** LAST_RESULT) - number:
    print('Ближайшую степень двойки к введенному числу', (2 ** LAST_RESULT))
else:
    print('Ближайшую степень двойки к введенному числу', (2 ** PREVIOUS))
