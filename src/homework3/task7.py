"""
Анаграммы
"""
s1 = input("Введите первое слово").lower()
s2 = input("Введите второе слово").lower()

name_1 = list(s1)
name_2 = list(s2)
name_2.sort()
name_1.sort()

if name_1 == name_2:
    print("Anagramma")
else:
    print("not anagramma")
