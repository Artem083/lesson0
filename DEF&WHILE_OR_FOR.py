# Пример кратности(деления без остатка):
# 1 + 2 = 3 (сумма пары)
# 9 / 3 = 3 (ровно 3 без остатка)
# 9 кратно 3 (9 делится на 3 без остатка)
#
#
# Пример 1:
# 9 - число из первой вставки
# 1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
#
# Пример 2:
# 11 - число из первой вставки
# 11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)
#
#
#
# Что является парой?:
# Пары являются уникальными на примере следующего:
# 7 3 3 5 8
# В этой последовательности уникальными парами являются:
# Для первой 7: 73 73 75 78
# Для второй 3: 33 35 38 (с первой 7 у этой 3 уже есть пара, поэтому её не берём).
#
# Все пароли для чисел от 3 до 20 (для сверки):
# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911
#
# Отдельно по числам, для большего понимания:
# 3 - 1+2
# 4 - 1+3
# 5 - 1+4 2+3
# 6 - 1+2 1+5 2+4
# 7 - 1+6 2+5 3+4
# 8 - 1+3 1+7 2+6 3+5
# ...
# 18 - 1+2 1+5 1+8 1+17 2+4 2+7 2+16 3+6 3+15 4+5 4+14 5+13 6+12 7+11 8+10
# 19 - 1+18 2+17 3+16 4+15 5+14 6+13 7+12 8+11 9+10
# 20 - 1+3 1+4 1+9 1+19 2+3 2+8 2+18 3+7 3+17 4+6 4+16 5+15 6+14 7+13 8+12 9+11
# Примечания:
# Можно использовать как цикл for, так и цикл while
# Первое число не входит в одно из чисел пары
# Пары чисел подбираются от 1 до 20 для текущего числа.

import random


def get_cipher():  # получим число первого поля
    _num_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher


def get_passcode(e):
    passdict = {}  # создаём словарь с кодами и паролями
    passdict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    passdict.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    passdict.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    passdict.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passdict.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    passdict.update({20: 13141911923282183731746416515614713812911})
    passcode = passdict.get(e)
    return passcode


n = get_cipher()
# n = int(input('введите шиифр :'))
print('Шифр   :', n)
# print('Пароль :', get_passcode(n))

pairnum1 = list(range(1, n))
pairnum2 = list(range(1, n))
pairs = []
result = ''

for i in pairnum1:
    for j in pairnum2:
        pn1 = i  # pairnum1[i]
        pn2 = j  # pairnum2[j]
        if pn1 >= pn2:
            continue
        else:
            kratno = n % (pn1 + pn2)
            if kratno == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *pairs)
print('Введите пароль', result, 'во вторую вставку')
if int(result) == get_passcode(n):
    print('Ура!')
    print('Подошёл!!! Пароль ПОДОШЁЛ!')
    print('Мы спасены! Свобода!')
