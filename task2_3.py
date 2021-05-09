# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


# 1, 3, -2
def split(word):
    return [character for character in word]


for index in (1, -2):
    if len(my_list[index]) > 1:
        symbols = split(my_list[index])
        my_list[index] = '0'.join(symbols)
    else:
        my_list[index] = '0' + my_list[index]

for index in (1, 3, 5, 7, -2, -1):
    my_list.insert(index, '"')
list_is_processed = ' '.join(my_list)
# 4, 7, -11, -15, 17, 20
print(list_is_processed)
hour = '05'
minute = '17'
first_part = list_is_processed[:3]
second_part = list_is_processed[7:17]
third_part = list_is_processed[20:]
print(f'{first_part}{hour}{second_part}{minute}{third_part}')
