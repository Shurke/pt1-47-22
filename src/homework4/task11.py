"""
Набор данных, содержащий детские имена, состоит более чем из 200 файлов, в каждом из которых, помимо
сотни имен, указано количество названных тем или иным именем детей. При этом файлы отсортированы по
убыванию популярности имен. Для каждого года присутствует по два файла: в одном перечислены мужские
имена, в другом – женские. Совокупный набор данных содержит информацию для всех лет, начиная с
1900-го и заканчивая 2012-м.

Напишите программу, которая будет считывать данные (baby_names.zip) и предоставлять следующие
результаты:
    имена, которые были лидерами (топ-10) по частоте использования как минимум в одном году. На
    выходе должно получиться два списка: в одном из них будут присутствовать наиболее популярные
    имена для мальчиков, во втором – для девочек. При этом списки не должны содержать повторяющиеся
    имена.

    имена, использованные для мальчиков и девочек (универсальные имена). Если в этом году
    универсальных имен не было, нужно известить об этом пользователя. Кроме того, если за указанный
    пользователем год не было данных по именам, выведите соответствующее сообщение об ошибке.

Предусмотреть возможность работать с каким-то ограниченным периодом времени или с конкретным годом.
Например, ваша программа должна корректно вывести данные, если пользователь ввел “1990-1995” или
просто “1996”. Если пользователем на вход программы не передал никаких данных, то необходимо вывести
все данные за все время.
"""


import zipfile
import heapq


def main():
    def get_period_range(period='') -> tuple:
        """Converts the input string to a tuple with dates.

        :param period: input string in format "1900-2000"
        :return: tuple with dates
        """

        if period == '':
            date_tuple = tuple(range(1900, 2023))
        elif len(period) == 4:
            date_tuple = (int(period)),
        elif len(period) == 9:
            start_date = int(period[:4])
            end_date = int(period[5:])
            date_tuple = tuple(range(start_date, end_date + 1))
        else:
            print('Some trouble with period')
            raise ValueError()

        return date_tuple

    def get_data_from_file(period: tuple, file_name='baby_names.zip') -> dict:
        """Return dict with data for period or False

        :param period: period of search (use get_period_range())
        :param file_name: archive database name, default = baby_names.zip
        :return: dict of baby names in search period
        """

        z = zipfile.ZipFile(file_name, 'r')

        name_in_years_dict = {}

        for file_name in z.namelist():
            if int(file_name[10:14]) in period:
                with z.open(file_name, 'r') as opened_file:
                    file_content = opened_file.readlines()
                    file_dict_with_name_frequency = {}
                    for elem in file_content:
                        elem_list = elem.decode()[:-2].split()
                        file_dict_with_name_frequency[elem_list[0]] = int(elem_list[1])
                    name_in_years_dict[tuple(file_name[10:16].split('_'))] = \
                        file_dict_with_name_frequency

        return name_in_years_dict

    def get_tuple_of_popular_name(input_dict: dict):
        """Return tuple with most popular (top 10) names from input_dict

        :param input_dict: dict of baby names (use get_data_from_file())
        :return: tuple with sets in form (girls_popular_names, boys_popular_names)
        """
        g_pop_names = set()
        b_pop_names = set()
        for year_gender, names in input_dict.items():

            most_popular_in_num = heapq.nlargest(10, names.values())
            for name, num in names.items():
                if num in most_popular_in_num:
                    if year_gender[1] == 'G':
                        g_pop_names.add(name)
                    else:
                        b_pop_names.add(name)

        return g_pop_names, b_pop_names

    def print_generic_name(input_dict: dict) -> set:
        """Return set with unique generic names from input_dict

        :param input_dict: dict of baby names (use get_data_from_file())
        :return: set with unique generic names
        """
        g_name_set = set()
        b_name_set = set()
        for year_gender, names in input_dict.items():
            for name in names.keys():
                if year_gender[1] == 'G':
                    g_name_set.add(name)
                else:
                    b_name_set.add(name)
        generic_set = g_name_set.intersection(b_name_set)

        return generic_set

    while True:
        per = input('Please type an interval, leave empty if you would like to see the data for'
                    ' all time, or exit: ')
        if per != 'exit':
            try:
                period_tuple = get_period_range(period=per)
                if len(period_tuple) != 1:
                    print(f'Search data for {period_tuple[0]}-{period_tuple[-1]}')
                else:
                    print(f'Search data for {period_tuple[0]}')
                y_dict = get_data_from_file(period=period_tuple)
                pop_names = get_tuple_of_popular_name(y_dict)
                print(f'Most popular girl names is: {", ".join(pop_names[0])}')
                print(f'Most popular boy names is: {", ".join(pop_names[1])}')
                set_of_generic = print_generic_name(y_dict)
                if set_of_generic:
                    print(f'Generic names: {", ".join(set_of_generic)}')
                else:
                    print('No generic names.')
            except KeyError:
                print('In my opinion you made a mistake in year.')
            except (ValueError, AttributeError):
                print('In my opinion you made a mistake in date.')
            except Exception as exc:  # debug
                print(type(exc))
                print('In my opinion you made a mistake... Somewhere.')
        else:
            exit('Closed by user')


if __name__ == '__main__':
    main()
