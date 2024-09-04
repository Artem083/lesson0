def get_matrix(n, m, value):              # 1.Объявите функцию get_matrix и напишите в ней параметры n, m и value.
    matrix_ = []                          # 2.Создайте пустой список matrix внутри функции get_matrix.
    for i in range(n):                    # 3.Напишите перв.(внеш.) цикл for для кол-ва строк мат-цы, n повторов.
        matrix_.append([])                # 4.В первом цикле добавляйте пустой список в список matrix.
        for j in range(m):                # 5.Напишите втор.(внутр.) цикл for для кол-ва столбцов матрицы, m повторов.
            matrix_[i].append(value)      # 6.Во втором цикле пополняйте ранее добавленный пустой список знач-ями value.
    return matrix_                        # 7.После всех циклов верните значение переменной matrix.


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)         # 8.Выведите на экран(консоль) результат работы функции get_matrix.
print(result2)
print(result3)
