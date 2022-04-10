"""
Порядковая дата содержит номер года и порядковый номер дня в этом году – оба в целочисленном
формате. При этом год может быть любым согласно григорианскому календарю, а номер дня – числом в
интервале от 1 до 366 (чтобы учесть високосные годы). Порядковые даты удобно использовать при
расчете разницы в днях, когда счет ведется именно в днях, а не месяцах. Например, это может касаться
90-дневного периода возврата товара для покупателей, расчета срока годности товаров или
прогнозируемой даты появления малыша на свет.
Напишите функцию с именем ordinal_date, принимающую на вход три целых числа: день, месяц и год.
Функция должна возвращать порядковый номер заданного дня в указанном году. В основной программе у
пользователя должны запрашиваться день, месяц и год соответственно и выводиться на экран порядковый
номер дня в заданном году. Программа должна запускаться только в том случае, если она не
импортирована в виде модуля в другой файл.
"""


def ordinal_date(day, month, year):
    """
    returns the sequence number of the day in the entered year
    :param day: day from user
    :param month: month from user
    :param year: year from user
    :return:
    """
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    temporary_month_sum = 0
    for elem in range(month - 1):
        temporary_month_sum += month_days[elem]

    return f'Number of the day {temporary_month_sum + day}'


user_day = int(input('Enter the day you wish: '))
user_month = int(input('Enter the month you wish: '))
user_year = int(input('Enter the year you wish: '))
print(ordinal_date(user_day, user_month, user_year))
