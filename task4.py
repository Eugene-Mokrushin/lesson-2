# 4. Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком? DONE
# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' DONE
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

example_list = ['test', '1', 'Sky', '345.90', 'no', 'FLOWER', '6', '456234.12']
for value in example_list:
    try:
        integer_number = int(value)
        print(integer_number)
    except ValueError:
        x = None
print('Все целочисленные наверху')

for value in example_list:
    try:
        float_number = float(value)
        if float_number % 1 != 0:
            print(float_number)
    except ValueError:
        x = None
print('Все рациональные наверху')
# Как модифицировать это условие для чисел со знаком? !!! знаком после запятой?

employee_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
all_employees = []

for index in employee_list:
    list_of_vacancy = index.split(' ')
    employee_name = list_of_vacancy[-1]
    name = employee_name.title()
    all_employees.append(name)
    print(f'Привет, {name}!')

print('Можно не создавать список - убрать 38 строку. Но вот список:')
print(all_employees)
