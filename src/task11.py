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


def catalog(year, gender):
    """Функция возвращает список имен в зависимости от пола и года"""
    with zipfile.ZipFile('baby_names.zip', 'r') as catallog_of_baby_names:
        with catallog_of_baby_names.open(f"BabyNames/{int(year)}_{gender}.txt") as list_names:
            result = [name.decode().split(None, 1)[0] for name in list_names]
    return result


def top10_names_gender(list_names, boys_and_girls):
    """Функция возвращает спииски топ 10 имен"""
    counter_names = 0
    top10_names = []
    while len(top10_names) < 10:
        if list_names[counter_names] not in boys_and_girls:
            top10_names.append(list_names[counter_names])
        counter_names += 1
    return top10_names


def top_10_names(year):
    """Функция возвращает спииски топ 10 имен мальчиков девочек и универсальные имена при наличии"""
    boys = 'BoysNames'
    girl = 'GirlsNames'
    list_boys = catalog(year, boys)
    list_girls = catalog(year, girl)
    boys_and_girls = [name for name in list_boys if name in list_girls]
    top10_boys = top10_names_gender(list_boys, boys_and_girls)
    top10_girls = top10_names_gender(list_girls, boys_and_girls)

    return top10_boys, top10_girls, boys_and_girls


def sorting_reduction(items):
    """Функция сортирует и сокращает список имен для периода времени"""
    result = []
    sort_dict = {x: items.count(x) for x in items}
    for key, item in sorted(sort_dict.items(), key=lambda x: x[1], reverse=True):
        if item != 0:
            result.extend([key])
    return result


def result_for_period(names_girls, names_boys, names_boys_and_girls, year):
    """Функция выводит результатвы за период времени"""
    print(f"Топ 10 имен для мальчиков за период {year[0]}-{year[1]}: "
          f"{sorting_reduction(names_boys)[:10]}")
    print(f"Топ 10 имен для девочек за период {year[0]}-{year[1]}: "
          f"{sorting_reduction(names_girls)[:10]}")
    print(f"Популярные универсальные имена за период {year[0]}-{year[1]}: "
          f"{sorting_reduction(names_boys_and_girls)}")


def years(year):
    """Функция выводит передает номер года относительно введенных пользователем"""
    names_boys = []
    names_girls = []
    names_boys_and_girls = []
    if year == "":
        for num_of_year in range(1900, 2013):
            list_names = (top_10_names(num_of_year))
            names_boys += list_names[0]
            names_girls += list_names[1]
            names_boys_and_girls += list_names[2]
        result_for_period(names_girls, names_boys, names_boys_and_girls, year=['1900', '2012'])
    else:
        year = year.split("-")
        if len(year) == 2:
            if int(year[0]) and int(year[1]) in range(1900, 2013):
                for num_of_year in range(int(year[0]), int(year[1]) + 1):
                    list_names = (top_10_names(num_of_year))
                    names_boys += list_names[0]
                    names_girls += list_names[1]
                    names_boys_and_girls += list_names[2]
                result_for_period(names_girls, names_boys, names_boys_and_girls, year)
            else:
                print("Вы ввели интервал выходящий за пределы базыданных")

        elif len(year) == 1:
            if int(year[0]) in range(1900, 2013):
                list_names = top_10_names(year[0])
                print(f"Топ 10 имен для мальчиков в {year} году: {list_names[0]}")
                print(f"Топ 10 имен для девочек в {year} году: {list_names[1]}")
                if len(list_names[2]) > 0:
                    print(f"Топ универсальных имен в {year} году: {list_names[2]}")
                else:
                    print(f"В {year} году не было универсальных имен")
            else:
                print(f"О именах в {year[0]} году нет данных")


if __name__ == '__main__':
    input_year = input("Введите интересующей вас год в пределах от 1900 до 2012: ")
    years(input_year)
