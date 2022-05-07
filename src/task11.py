"""Детские имена
Набор данных, содержащий детские имена, состоит более чем из 200 файлов, в каждом из которых,
помимо сотни имен, указано количество названных тем или иным именем детей. При этом файлы
отсортированы по убыванию популярности имен. Для каждого года присутствует по два файла: в одном
перечислены мужские имена, в другом – женские. Совокупный набор данных содержит информацию для
всех лет, начиная с 1900-го и заканчивая 2012-м.
Напишите программу, которая будет считывать данные (baby_names.zip) и предоставлять следующие
результаты:
имена, которые были лидерами (топ-10) по частоте использования как минимум в одном году. На выходе
должно получиться два списка: в одном из них будут присутствовать наиболее популярные имена для
мальчиков, во втором – для девочек. При этом списки не должны содержать повторяющиеся имена.
имена, использованные для мальчиков и девочек (универсальные имена). Если в этом году универсальных
имен не было, нужно известить об этом пользователя. Кроме того, если за указанный пользователем год
не было данных по именам, выведите соответствующее сообщение об ошибке.
Предусмотреть возможность работать с каким-то ограниченным периодом времени или с конкретным годом.
Например, ваша программа должна корректно вывести данные, если пользователь ввел “1990-1995” или
просто “1996”. Если пользователем на вход программы не передал никаких данных, то необходимо
вывести все данные за все время.
"""

import zipfile


def top_10_names(year):
    """Функция возвращает спииски топ 10 имен

    :списки имен мальчиков,девочек и если есть в этом году универсльные имена выводит их отдельно
    :year: год по которому нужно создать топ 10 имен
    """
    with zipfile.ZipFile('baby_names.zip', 'r') as catallog_of_baby_names:
        boys = catallog_of_baby_names.open(f"BabyNames/{int(year)}_BoysNames.txt")
        girls = catallog_of_baby_names.open(f"BabyNames/{int(year)}_GirlsNames.txt")
    list_boys = [name.decode().split(None, 1)[0] for name in boys]
    list_girls = [name.decode().split(None, 1)[0] for name in girls]
    boys_and_girls = [name for name in list_boys if name in list_girls]
    top10_boys = []
    top10_girls = []
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
    print(f"Топ 10 имен для мальчиков в {year} году: {top10_boys}")
    print(f"Топ 10 имен для девочек в {year} году: {top10_girls}")
    if len(boys_and_girls) > 0:
        print(f"Топ универсальных имен в {year} году: {boys_and_girls}")
    else:
        print(f"В {year} году не было универсальных")


def years(year):
    """Функция выводит передает номер года относительно введенных пользователем"""
    if year == "":
        for num_of_year in range(1900, 2013):
            top_10_names(num_of_year)
    else:
        year = year.split("-")
        if len(year) == 2:
            for num_of_year in range(int(year[0]), int(year[1]) + 1):
                if num_of_year in range(1900, 2013):
                    top_10_names(num_of_year)
                else:
                    print(f"О именах в {num_of_year} году нет данных")
        elif len(year) == 1:
            if int(year[0]) in range(1900, 2013):
                top_10_names(year[0])
            else:
                print(f"О именах в {year[0]} году нет данных")


input_year = input("Введите интересующей вас год: ")
years(input_year)
