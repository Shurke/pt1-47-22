"""Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое. 75 семей
 выписывают газету, 27 - журнал, 13 - и журнал, и газету. Сколько семей живет в доме N? Задачу
  решать с помощью множеств и их методов.
"""

newspapper = set(range(75))
journal = set(range(27))
newspapper_and_journal = set(range(13))

newspapper.difference_update(newspapper_and_journal)
journal.difference_update(newspapper_and_journal)

print(f'Количество семей: {len(newspapper) + len(journal) + len(newspapper_and_journal)}')
