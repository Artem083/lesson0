# def test_func(*params):
#     print("Тип", type(params))
#     print("Аргумент", params)
#
#
# test_func(1, 2, 3, 4)

# def summator(txt, *values, type_="sum"):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type_}'
#
#
# print(summator("Сумма чисел: ", 2, 3, 4, type_="summator"))


def info(**values):
    print("Тип", type(values))
    print("Аргумент", values)


info(name="Denis", course="Python")