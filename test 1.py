def summator(txt, *values):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}{type}'

print(summator("Сумма чисел: ",1, 2, 3, 4))