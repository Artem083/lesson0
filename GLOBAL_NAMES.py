calls = 0   # 1.Создать переменную calls = 0 вне функций.


def count_calls():   # 2. Создать функцию count_calls и изменять в ней значение переменной calls.
    global calls     # Эта функция должна вызываться в остальных двух функциях.
    calls += 1       # Функция count_calls подсчитывающая вызовы остальных функций.


def string_info(string):   # 3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
    stroka = str(string)     # Функция string_info принимает аргумент - строку и возвращает кортеж из:
    result = (len(stroka)), stroka.upper(), stroka.lower()   # длины этой строки, строку в верхнем регистре,
    count_calls()              # строку в нижнем регистре.
    return result


def is_contains(string, list_to_search):  # 4. Создать функцию is_contains с двумя параметрами string и list_to_search,
    string = str(string).lower()  # реализовать логику работы по описанию.
    list_to_search = list(list_to_search)   # Функция is_contains принимает два аргумента: строку и список,
    count_calls()   # и возвращает True, если строка находится в этом списке, False - если отсутствует.
    for i in range(len(list_to_search)):  # Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('capybara'))    # Вызвать соответствующие функции string_info и is_contains
print(string_info('Armageddon'))   # произвольное кол-во раз с произвольными данными.
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)