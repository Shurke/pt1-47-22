"""
Набор данных, содержащий детские имена, состоит более чем из 200 файлов, в каждом из которых, помимо
сотни имен, указано количество названных тем или иным именем детей. При этом файлы отсортированы по
убыванию популярности имен. Для каждого года присутствует по два файла: в одном перечислены мужские
имена, в другом – женские. Совокупный набор данных содержит информацию для всех лет, начиная с
1900-го и заканчивая 2012-м.
Напишите программу, которая будет считывать данные (baby_names.zip) и предоставлять следующие
результаты:
имена, которые были лидерами (топ-10) по частоте использования как минимум в одном году. На выходе
должно получиться два списка: в одном из них будут присутствовать наиболее популярные имена для
мальчиков, во втором – для девочек. При этом списки не должны содержать повторяющиеся имена,
использованные для мальчиков и девочек (универсальные имена). Если в этом году универсальных имен не
было, нужно известить об этом пользователя. Кроме того, если за указанный пользователем год
не было данных по именам, выведите соответствующее сообщение об ошибке.
Предусмотреть возможность работать с каким-то ограниченным периодом времени или с конкретным годом.
Например, ваша программа должна корректно вывести данные, если пользователь ввел “1990-1995” или
просто “1996”. Если пользователем на вход программы не передал никаких данных, то необходимо вывести
все данные за все время.
"""

import zipfile


def open_file(year, file='baby_names.zip'):
    """Open file and create a dict with boys and girls data

    :param year: list from func get_years
    :param file: datafile
    :return: dict with boys and girls names in input years
    """
    boys_and_girls_dict = {}
    year_for_func = [int(elem) for elem in year]
    try:
        with zipfile.ZipFile(file, 'r') as database:
            for file in database.namelist():
                if int(file[10:14]) in year_for_func:
                    boys_and_girls = database.open(file, 'r').readlines()
                    data_dict = {}
                    for elem in boys_and_girls:
                        data_lst = elem.decode().rstrip().split()
                        data_dict[data_lst[0]] = int(data_lst[1])
                    boys_and_girls_dict[tuple(file[10:19].split('_'))] = data_dict
    except FileNotFoundError:
        print('File error')
    return boys_and_girls_dict


def get_top_names(dict_years_names):
    """Print the most popular (top 10) names from open file and universal name in range input years

    :param dict_years_names: dict with boys and girls from open_file
    :return: set with top-10 boys, set with top-10 girls, set with universal names
    """

    boy_top_set = set()
    girl_top_set = set()
    b_unique_set = set()
    g_unique_set = set()

    for year_gender, names in dict_years_names.items():
        for name in names.keys():
            if year_gender[1] == 'Boys':
                b_unique_set.add(name)
            else:
                g_unique_set.add(name)

    universal_set = b_unique_set & g_unique_set

    for year_gender, names in dict_years_names.items():
        top_lst = list(names.keys())[:10]
        for top_name, year in names.items():
            if top_name in set(top_lst) and top_name not in universal_set:
                if year_gender[1] == 'Boys':
                    boy_top_set.add(top_name)
                else:
                    girl_top_set.add(top_name)

    return universal_set, boy_top_set, girl_top_set


def output(years, universal_names, boys, girls):
    """Output of the top 10 boys' and girls' names in the given years.

    Output of universal names in the given years

    :param years: list from func get_years
    :param universal_names: universal_set from get_top_names
    :param boys: set with top-10 boys names from get_top_names
    :param girls: set with top-10 girls names from get_top_names
    """
    if universal_names:
        if len(years) == 1:
            print(f'Universal names in this {years[0]} year were {", ".join(universal_names)} ')
        else:
            print(f'Universal names in this {years[0]}-{years[-1]} period were'
                  f' {", ".join(universal_names)} ')
    else:
        print(f'In this {years[0]}-{years[-1]} period were not universal names')

    if len(years) == 1:
        print(f'Top-10 boys names in the {years[0]} year: {", ".join(boys)}.')
        print(f'Top-10 girls names in the {years[0]} year: {", ".join(girls)}.')
    else:
        print(f'Top-10 boys names in the {years[0]}-{years[-1]} year: {", ".join(boys)}.')
        print(f'Top-10 girls names in the {years[0]}-{years[-1]} year: {", ".join(girls)}.')


def get_years(year):
    """Convert string from user to necessary view

    :param year: string with years from user
    :return: list with years
    """
    correct_year = []
    if year == '':
        for years in range(1900, 2013):
            correct_year.append(years)
    else:
        year = year.split('-')
        if len(year) == 2:
            for years in range(int(year[0]), int(year[1]) + 1):
                if int(year[0]) >= 1900 and int(year[1]) <= 2012:
                    correct_year.append(years)
                else:
                    print(f'This {", ".join(year)} period are not in database')
                    raise ValueError
        elif len(year) == 1:
            if 1900 <= int(year[0]) <= 2012:
                correct_year.append(year[0])
            else:
                print(f'This {", ".join(year)} period is not in database')
                raise ValueError
    return correct_year


def main():
    years_from_user = input('Enter the prefer year in range 1900-2012 like "1990-1995" or "1996": ')
    convert_year = get_years(years_from_user)
    names_dict = open_file(convert_year, file='baby_names.zip')
    universal_names, boy_top_names, girl_top_names = get_top_names(names_dict)
    output(convert_year, universal_names, boy_top_names, girl_top_names)


if __name__ == '__main__':
    main()
