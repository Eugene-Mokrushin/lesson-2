# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»).DONE
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).DONE
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).DONE
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.DONE
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
# DONE
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.

import random


def paragraph():
    print('-' * 500)


def prices_list(beginning, end, length):
    float_list = []
    unique_set = set()
    for i in range(length):
        x = round(random.uniform(beginning, end), 2)
        while x in unique_set:
            x = round(random.uniform(beginning, end), 2)
        unique_set.add(x)
        float_list.append(x)

    return float_list


def make_readable(prices):
    correctly_written_prices_list = []
    for price in prices:
        rubble = price // 1
        rubble = int(rubble)
        penny = (price * 100) % 100
        penny = int(penny)
        if len(str(rubble)) < 2:
            rubble = '0' + str(rubble)
        if len(str(penny)) < 2:
            penny = '0' + str(penny)
        correctly_written_prices_list.append(f'{rubble} руб {penny} коп')
    correctly_written_prices = ', '.join(correctly_written_prices_list)
    return correctly_written_prices


cost = prices_list(0, 100, random.randint(10, 20))

paragraph()
print('Все цены товаров')
print(make_readable(cost))

paragraph()
cost.sort()
print('Цены отсортированный в порядке возрастания')
print(make_readable(cost))

paragraph()
prices_to_cheaper = cost.copy()
prices_to_cheaper.sort()
prices_to_cheaper.reverse()
print('Список цен по убыванию')
print(make_readable(prices_to_cheaper))

paragraph()
print('Пять самых дорогих товаров')
print(make_readable(prices_to_cheaper[:5]))
