"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

a = input("Введите данные:")
BIG = LTL = 0
for char in list(a.replace(" ", "")):
    if 65 <= ord(char) <= 90:
        BIG += 1
    else:
        LTL += 1
print(F"прописных {BIG} строчных {LTL}")
