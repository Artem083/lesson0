first = int(input('Введите целое число '))  # - Если равных чисел среди 3-х вообще нет, то вывести 0
second = int(input('Ввведите целое число '))
third = int(input('Введите целое число '))
if first != second and first != third and second != third:
    print(0)
elif first == second and not first == third:  # - Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
    print(2)
elif first == third and not second == first:
    print(2)
elif second == third and not first == second:
    print(2)
else:
    print(3)    # - Если все числа равны между собой, то вывести 3