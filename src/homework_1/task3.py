"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

a = input("Введите строку")
BIG = 0
SMALL = 0
ANOTHER = 0
for i in a:
    if 'a' <= i <= 'z':
        SMALL += 1
    elif 'A' <= i <= 'Z':
        BIG += 1
    else:
        ANOTHER += 1
print(BIG, "Кол-во заглавных бук")
print(SMALL, "Кол-во строчных букв")
print(ANOTHER, "Кол-во неверно введенных символов")
