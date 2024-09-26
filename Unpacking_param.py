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
def print_params(a: any = 1, b: any = 'строка', c: any = True):  # 1.Функция с параметрами по умолчанию:
    print(a, b, c)


print_params(5, 'kdjjk')  # Вызовите функцию print_params с разным количеством аргументов,
print_params(8)
print_params(2, 'jhlfksjh', False)
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

spisok_list = [99, 126, 'закорючка']
spisok_dict = {'a': 99, 'b': 126, 'c': 'шлямбур'}
print_params(*spisok_list)
print_params(**spisok_dict)

# 3.Распаковка + отдельные параметры:
# Создайте список values_spisok_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_spisok_2, 42)

values_list2 = (54.32, 'Строка')
print_params(*values_list2, 42)
