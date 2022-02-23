"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Сколько семей живет в доме N? Задачу решать с помощью множеств и их методов.
"""


newspapers = set(range(75))
magazines = set(range(27))
news_and_magaz = set(range(13))

newspapers.difference_update(news_and_magaz)
magazines.difference_update(news_and_magaz)

residents = len(newspapers) + len(magazines) + len(news_and_magaz)
print(f'Количество семей проживающих в доме N - {residents}')
