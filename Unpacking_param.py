# Домашнее задание по уроку "Распаковка позиционных параметров".
# Цель задания: Освоить создание функций с параметрами по умолчанию
# и практику вызова этих функций с различным количеством аргументов.
# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True),
# которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
def print_params(a=1, b='строка', c=True):  # 1.Функция с параметрами по умолчанию:
    print(a, b, c)


print_params(5, 'kdjjk')  # Вызовите функцию print_params с разным количеством аргументов,
print_params(8)
print_params(2, 'jhlfksjh', False)
print_params('Zachem')
print_params(True)
print_params(0)
print_params()  # включая вызов без аргументов.
print_params(b=25)  # Проверьте, работают ли вызовы print_params(b = 25)
print_params(c=[1, 2, 3])  # print_params(c = [1,2,3])

# 2.Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params,
# и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params,
# используя распаковку параметров (* для списка и ** для словаря).

spisok_list = [99, 126, 'закорючка', False]
spisok_dict = {'a': 99, 'b': 126, 'c': 'шлямбур', 'd': True}


def print_params(*values_list, **values_dict):
    print(*values_list)
    return values_dict


print_params(*spisok_list, **spisok_dict)

# 3.Распаковка + отдельные параметры:
# Создайте список values_spisok_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_spisok_2, 42)

values_list2 = (54.32, 'Строка')


def print_params(*valueslist_2):
    print(*valueslist_2)


print_params(*values_list2, 42)

#   ЛЕКЦИЯ ДЕНИСА ПИКАЕВА
# def print_params(a, b, c):   # *args, **kwargs
#     print(a, b, c)

# def print_params(*args):   # *args, **kwargs
#     print(a, b, c)


# def print_params(*params):   # *args, **kwargs
#     print(*params)
#
#
# print_params(1, 2, 3, 4, 5, 6, 7)


# def print_params(*params):   # *args, **kwargs
#     print(*params)
#
#
# print_params()


# def print_params(a, b, c):   # *args, **kwargs
#     print(a, b, c)
#     print(c)
#
# list_ = [1, 2]
# print_params(*list_, 4)


# def print_params(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# dict_ = {'a': 1, 'b': 2, 'd': 3,}
# print_params(**dict_)


# def print_params(a, b, c):    # *args, **kwargs
#     print(a, b, c)
#
#
# list_ = [1, 2]
# dict_ = {'c': 3}
# print_params(*list_, **dict_)
