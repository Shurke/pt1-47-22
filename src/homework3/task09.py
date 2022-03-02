"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Сколько семей живет в доме N? Задачу решать с помощью множеств и их методов.
"""


newspaper_subscriber = 75
journal_subscriber = 27
journal_n_newspaper = 13

newspaper = set(range(newspaper_subscriber))
journal = set(range(journal_subscriber))
both = len(set(range(journal_n_newspaper)))

total = len(newspaper) + len(journal)
families = total - both
print(f'Количество семей в доме: {families}')
