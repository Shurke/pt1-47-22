"""Случайные лотерейные номера"""

import random
a = 6
b = []
while a > len(b):
    c = random.randint(1, 49)
    if c not in b:
        b.append(c)
print("Выйгрышное число :", sorted(b))
