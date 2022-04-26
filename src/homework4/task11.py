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
    boys_years_dict = {}
    girls_years_dict = {}
    year_for_func = [int(elem) for elem in year]
    for years in year_for_func:
        try:
            with zipfile.ZipFile(file, 'r') as database:
                boys = database.open(f'BabyNames/{years}_BoysNames.txt')
                boys_dict = {}
                for boy_name in boys:
                    boys_lst = boy_name.decode().rstrip().split()
                    boys_dict[boys_lst[0]] = int(boys_lst[1])
                boys_years_dict[years] = boys_dict
                girls = database.open(f'BabyNames/{years}_GirlsNames.txt')
                girls_dict = {}
                for girl_name in girls:
                    girls_lst = girl_name.decode().rstrip().split()
                    girls_dict[girls_lst[0]] = int(girls_lst[1])
                girls_years_dict[years] = girls_dict
                boys.close()
                girls.close()
        except FileNotFoundError:
            print('File error')
    return boys_years_dict, girls_years_dict


def get_top_names(boy_dict, girl_dict):
    """Print the most popular (top 10) names from open file and universal name in range input years

    :param : list from func get_years
    :param boy_dict: dict with boys from open_file
    :param girl_dict: dict with girls from open_file
    :return: set with top-10 boys, set with top-10 girls, set with universal names
    """

    boy_top_set = set()
    girl_top_set = set()
    b_unique_set = set()
    g_unique_set = set()
    for b_year, b_names in boy_dict.items():
        for b_name in b_names.keys():
            b_unique_set.add(b_name)
    for g_year, g_names in girl_dict.items():
        for g_name in g_names.keys():
            g_unique_set.add(g_name)
    universal_set = b_unique_set & g_unique_set

    for b_year, b_names in boy_dict.items():
        b = list(b_names.keys())[:10]
        for b_temp_name in b_names.keys():
            if b_temp_name in set(b) and b_temp_name not in universal_set:
                boy_top_set.add(b_temp_name)

    for g_year, g_names in girl_dict.items():
        g = list(g_names.keys())[:10]
        for g_temp_name in g_names.keys():
            if g_temp_name in set(g) and g_temp_name not in universal_set:
                girl_top_set.add(g_temp_name)

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
                if years in range(1900, 2013):
                    correct_year.append(years)
                else:
                    print(f'This {year} period are not in database')
                    raise ValueError
        elif len(year) == 1:
            if int(year[0]) in range(1900, 2013):
                correct_year.append(year[0])
            else:
                print(f'This {year} period is not in database')
                raise ValueError
    return correct_year


def main():
    years_from_user = input('Enter the prefer year in range 1900-2012 like "1990-1995" or "1996": ')
    convert_year = get_years(years_from_user)
    names_dict = open_file(convert_year, file='baby_names.zip')
    names = get_top_names(names_dict[0], names_dict[1])
    output(convert_year, names[0], names[1], names[2])


if __name__ == '__main__':
    main()
