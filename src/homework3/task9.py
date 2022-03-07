"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое. 75 семей
выписывают газету, 27 - журнал, 13 - и журнал, и газету. Сколько семей живет в доме N?
Задачу решать с помощью множеств и их методов
"""

NEWSPAPER = set(range(75))
MAGAZINE = set(range(27))
MAG_NEWSP = set(range(13))
ONLY_NEWSP = len(NEWSPAPER.difference(MAG_NEWSP))
ONLY_MAG = len(MAGAZINE.difference(MAG_NEWSP))
QUANT_FAMILY = ONLY_NEWSP + ONLY_MAG + len(MAG_NEWSP)
print(f'Количество семей в доме: {QUANT_FAMILY}')
