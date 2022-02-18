'''
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое. 75 семей
выписывают газету, 27 - журнал, 13 - и журнал, и газету. Сколько семей живет в доме N? Задачу решать
с помощью множеств и их методов.
'''


NEWSPAPER = set(range(1, 76))
MAGAZINE = set(range(max(NEWSPAPER) + 1, max(NEWSPAPER) + 1 + 27))
ALL = set(range(1, 14))
N = len(NEWSPAPER.union(MAGAZINE).difference(ALL))
print(f'В доме N, где {len(NEWSPAPER)} семей выписывают газету, {len(MAGAZINE)} выписывают журнал,'
      f'а {len(ALL)} и то, и другое, всего проживает {N} семей!')
