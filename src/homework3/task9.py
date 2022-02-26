"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и
другое. 75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Сколько семей живет в доме N? Задачу решать с помощью множеств и их методов.
"""

newspaper = {int(item) for item in range(1, 76)}
journal = {int(item) for item in range(1, 28)}
new_jour = {int(item) for item in range(1, 14)}
only_newspaper = newspaper - new_jour
only_journal = journal - new_jour
print(f"В доме живёт {len(only_newspaper) + len(only_journal) + len(new_jour)}"
      f"семей")
