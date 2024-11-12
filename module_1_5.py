# 2. Задайте переменные разных типов данных.
immutable_var: tuple = 1, 2, 3, 'call', 'message', 'push', False
print(immutable_var)
print(type(immutable_var))
# 3. Изменение значений переменных.
# immutable_var[4] = 'sms'
# print(immutable_var)
# Traceback (most recent call last):
#  File "C:\Users\Ram_09-06-2020\Desktop\АРТЕМ\lesson0\module_1_5.py", line 6, in <module>
#    immutable_var  [4] = 'sms'
#    ~~~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# 4. Создание изменяемых структур данных.
mutable_list = [1, 2, 3, 'call', 'message', 'push', False]
mutable_list[4] = 'sms'
print(mutable_list)
print(type(mutable_list))
# Результат:
print('Immutable tuple' + ':', immutable_var)   # изменить четвёртое значение (message на sms) в кортеже не удаётся
print('Mutable list' + ':', mutable_list)     # Modified # четвёртое значение (message на sms) удалось изменить
