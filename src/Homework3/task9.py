"""Каждая семья, живущая в доме N, выписывает газету, или журнал,
или и то, и другое. 75 семей выписывают газету, 27 - журнал,
13 - и журнал, и газету. Сколько семей живет в доме N? Задачу
решать с помощью множеств и их методов."""


set_newspap = set(range(75))
set_magazin = set(range(max(set_newspap) + 1, (max(set_newspap) + 1) + 27))
set_news_and_mag = set(range(13))
set_family = set_newspap ^ set_news_and_mag
set_family = set_family ^ set_magazin
n_family = len(set_family)
print(f"В доме N проживает {n_family} семей")