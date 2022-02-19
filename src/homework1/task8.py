"""
Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B
включительно, в порядке убывания.
"""

A = int(input("Введите Ваше первое число: "))
B = int(input("Введите Ваше второе число: "))
if A % 2 != 0:
    for i in range(A, B - 1, -2):
        print(i)
else:
    for i in range(A - 1, B - 1, -2):
        print(i)

"""
Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил,
что находится на расстоянии x метров от одного из длинных бортиков (не
обязательно от ближайшего) и y метров от одного из коротких бортиков. Какое
минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна
на бортик? Программа получает на вход числа N, M, x, y. Программа должна вывести
число метров, которое нужно проплыть Яше до бортика.
"""

n = int(input("Введите первый параметр бассейна:"))
m = int(input("Введите второй параметр бассейна:"))
x = int(input("Введите расстояние, на котором Яша находится от длин. бортика:"))
y = int(input("Введите расстояние, на котором Яша находится от кор. бортика:"))

if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
if x < y:
    print(f"Яше необходимо проплыть {x} метров до ближайшего бортика")
else:
    print(f"Яше необходимо проплыть {y} метров до ближайшего бортика")

"""
По данному натуральному n вычислите сумму 1!+2!+3!+...+n!. В решении этой
задачи можно использовать только один цикл. Пользоваться математической
библиотекой math в этой задаче запрещено.
"""

n = int(input("Введите Ваши число: "))
i = 1
sum_1 = 0
b = 1
for i in range(1, n + 1):
    b *= i
    sum += b
print(f"Сумма равна: {sum_1}")

"""
Задания из нашего файла "Строковые операции строки"
Вводится строка. Удалить из нее все пробелы, после этого определить,
является ли она палиндромом, т.е. одинаково пишется как с начала так и с конца.
"""

a = input("Введите ваш текст: ")
b = a.split()
m = ("".join(b))
n = m[::-1]
if m == n:
    print("Ваш текст палиндром")
else:
    print("Ваш текст не палиндром")

"""
Найти самое длинное слово в введенном предложении
"""

a = input("Введите ваш текст: ")
b = max(a.split(), key=len)
print("Самое длинное слово", b)

"""
Уравнение прямой вида y = kx + b задано в виде строки. Определить координату
y точки с заданной координатой x.
"""

x = float(input("Введите координату x: "))
a = "y = 5x + 4"
b = a.split()
c = float(b[2].replace('x', '')) * float(x)
y = c + float(b[4])
print("y = ", y)

"""
Заменить все пробелы в строке на точки не используя replace.
"""

a = input("Введите ваш текст: ")
b = a.split()
print(".".join(b))

"""
Срезы.
Дана строка.
Сначала выведите третий символ этой строки.
Во второй строке выведите предпоследний символ этой строки.
В третьей строке выведите первые пять символов этой строки.
В четвертой строке выведите всю строку, кроме последних двух символов.
В пятой строке выведите все символы с четными индексами (считая, что индексация
начинается с 0,поэтому символы выводятся начиная с первого).
В шестой строке выведите все символы с нечетными индексами, то есть начиная со
второго символа строки.
В седьмой строке выведите все символы в обратном порядке.
В восьмой строке выведите все символы строки через один в обратном порядке,
начиная с последнего.
В девятой строке выведите длину данной строки.
"""

a = 'abcdef'
print(a[2])
print(a[-2])
print(a[0:5])
print(a[0:4])
print(a[0::2])
print(a[1::2])
print(a[5::-1])
print(a[5::-2])
print(len(a))

"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
1 -->  1
2 --> 3 + 5 = 8
"""


def row_sum_odd_numbers(my_number):
    return my_number ** 3


"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted
string, the longest possible, containing distinct letters - each taken only
once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"
"""


def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


"""
Our football team finished the championship. The result of each match look like
"x:y". Results of all matches are recorded in the collection.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such collection and counts the points of our team in
the championship. Rules for counting points for each match:

if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
"""


def points(games):

    count = 0
    for score in games:
        res = score.split(':')
        if res[0] > res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count
