""" 9. Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету,
27 - журнал,
13 - журнал и газету.
Сколько семей живет в доме N?
Задачу решать с помощью множеств и их методов.
"""


newspapper_subscribers = set(range(75))
journal_subscribers = set(range(27))
both_subscribers = set(range(13))

newspapper_subscribers.difference_update(both_subscribers)
journal_subscribers.difference_update(both_subscribers)

subscribers_count = len(newspapper_subscribers) + len(journal_subscribers) + len(both_subscribers)

print(f"Семей проживающих в доме: {subscribers_count}")
