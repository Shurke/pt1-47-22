'''
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое. 75 семей
выписывают газету, 27 - журнал, 13 - и журнал, и газету. Сколько семей живет в доме N?
Задачу решать с помощью множеств и их методов.
'''


newspapers = {'n' + str(x) for x in range(1, 76)}
magazines = {'m' + str(y) for y in range(1, 28)}
i = 1
while len(newspapers & magazines) != 13:
    newspapers.discard('n' + str(i))
    newspapers.add('n_and_m' + str(i))
    magazines.discard('m' + str(i))
    magazines.add('n_and_m' + str(i))
    i += 1
print(f'В доме живет {len(newspapers | magazines)} семей')
