"""
Заданы две клетки шахматной доски. Если они покрашены в один цвет,
то выведите слово YES, а если в разные цвета — то NO.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой
клетки, потом для второй клетки.
"""


a = int(input('Введите X-координату первой клетки: '))
b = int(input('Введите Y-координату первой клетки: '))
c = int(input('Введите X-координату второй клетки: '))
d = int(input('Введите Y-координату второй клетки: '))

ab = (a + b) % 2
cd = (c + d) % 2

if ab == cd:
    print("YES")
else:
    print("NO")

"""
Шахматная ладья ходит по горизонтали или вертикали.
Даны две различные клетки шахматной доски, определите, может ли
ладья попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. Программа должна вывести YES, если из
первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
"""


a = int(input('Введите X-координату первой клетки: '))
b = int(input('Введите Y-координату первой клетки: '))
c = int(input('Введите X-координату второй клетки: '))
d = int(input('Введите Y-координату второй клетки: '))

if a == c or b == d:
    print("YES")
else:
    print("NO")

"""
Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
Даны две различные клетки шахматной доски, определите,
может ли ферзь попасть с первой клетки на вторую одним ходом.
"""


a = int(input('Введите X-координату первой клетки: '))
b = int(input('Введите Y-координату первой клетки: '))
c = int(input('Введите X-координату второй клетки: '))
d = int(input('Введите Y-координату второй клетки: '))
ac = abs(a - c)
bd = abs(b - d)

if ac == bd or a == c or b == d:
    print("YES")
else:
    print("NO")

"""
Шахматный конь ходит буквой “Г” — на две клетки по вертикали
в любом направлении и на одну клетку по горизонтали, или
наоборот. Даны две различные клетки шахматной доски,
определите, может ли конь попасть с первой клетки на вторую одним ходом.
"""


a = int(input('Введите X-координату первой клетки: '))
b = int(input('Введите Y-координату первой клетки: '))
c = int(input('Введите X-координату второй клетки: '))
d = int(input('Введите Y-координату второй клетки: '))
ac = abs(a - c)
bd = abs(b - d)

if ac == 1 and bd == 2 or bd == 1 and ac == 2:
    print("YES")
else:
    print("NO")

"""
Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил,
что находится на расстоянии x метров
от одного из длинных бортиков (не обязательно от ближайшего)
и y метров от одного из коротких бортиков.
Какое минимальное расстояние должен проплыть Яша,
чтобы выбраться из бассейна на бортик? Программа получает на вход
числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до бортика.
"""


N = int(input('Длина бассейка: '))
M = int(input('Ширина бассейна: '))
S_X = int(input('Расстояние до одного из длинных бортиков: '))
S_Y = int(input('Расстояние до одного из коротких бортиков: '))
MMAX = max(N, M)
MMIN = min(N, M)
N = MMAX - S_Y
M = MMIN - S_X
print(f'Минимальное расстояние до бортика: {min(S_X, S_Y, M, N)}')
