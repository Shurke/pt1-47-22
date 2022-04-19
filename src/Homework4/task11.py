"""Набор данных, содержащий детские имена, состоит более чем из 200 файлов,
в каждом из которых, помимо сотни имен, указано количество названных тем или
иным именем детей. При этом файлы отсортированы по убыванию популярности имен.
Для каждого года присутствует по два файла: в одном перечислены мужские имена,
в другом – женские. Совокупный набор данных содержит информацию для всех лет,
начиная с 1900-го и заканчивая 2012-м.
Напишите программу, которая будет считывать данные (baby_names.zip) и
предоставлять следующие результаты: имена, которые были лидерами (топ-10)
по частоте использования как минимум в одном году. На выходе должно получиться
два списка: в одном из них будут присутствовать наиболее популярные имена для
мальчиков, во втором – для девочек. При этом списки не должны содержать повторяющиеся
имена, использованные для мальчиков и девочек (универсальные имена). Если в этом году
универсальных имен не было, нужно известить об этом пользователя. Кроме того, если за
указанный пользователем год не было данных по именам, выведите соответствующее сообщение
об ошибке. Предусмотреть возможность работать с каким-то ограниченным периодом времени
или с конкретным годом. Например, ваша программа должна корректно вывести данные, если
пользователь ввел “1990-1995” или просто “1996”. Если пользователем на вход программы
не передал никаких данных, то необходимо вывести все данные за все время.
"""

import re
import zipfile


def top_names(year):

    """Данная функция обрабатывает каталог с именнами детей, создает список с именами детей."""

    catallog = zipfile.ZipFile("baby_names.zip", "r")
    list_boys = []
    list_girls = []
    boys = catallog.open(f"BabyNames/{int(year)}_BoysNames.txt")
    girls = catallog.open(f"BabyNames/{int(year)}_GirlsNames.txt")
    for name in boys:
        list_boys.append(re.sub('[^A-Za-z]', "", name.decode('utf-8')))
    for name in girls:
        list_girls.append(re.sub('[^A-Za-z]', "", name.decode('utf-8')))
    boys.close()
    girls.close()
    top10_boys = []
    top10_girls = []
    boys_and_girls = []
    for name in list_boys:
        if name in list_girls:
            boys_and_girls.append(name)
    counter_boys = 0
    counter_girls = 0
    while len(top10_boys) < 10:
        if list_boys[counter_boys] not in boys_and_girls:
            top10_boys.append(list_boys[counter_boys])
        counter_boys += 1
    while len(top10_girls) < 10:
        if list_girls[counter_girls] not in boys_and_girls:
            top10_girls.append(list_girls[counter_girls])
        counter_girls += 1
    print(f"топ 10 имен для мальчиков в {year} году \n{top10_boys}")
    print(f"топ 10 имен для девочек в {year} году \n{top10_girls}")
    if len(boys_and_girls) > 0:
        print(f"топ имен как для мальчиков так и для девочек"
              f" в {year} году \n{boys_and_girls}")
    else:
        print(f"в {year} году не было имен как для мальчиков так и для девочек")


def names_in_year(year):
    """Данная функция обрабатывает запрос пользователя по выбраному периоду(году)"""

    if year == "":
        for num in range(1900, 2013):
            top_names(num)
    else:
        year = year.split("-")
        if len(year) == 2:
            for num in range(int(year[0]), int(year[1]) + 1):
                if num in range(1900, 2013):
                    top_names(num)
                else:
                    print(f"на {num} год нет данных")
        elif len(year) == 1:
            if int(year[0]) in range(1900, 2013):
                top_names(year[0])
            else:
                print(f"на {year[0]} год нет данных")


your_year = input("Введите интересующей вас год\n")
names_in_year(your_year)
