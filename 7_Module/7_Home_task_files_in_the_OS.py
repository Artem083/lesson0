import os

print('Текущая директория', os.getcwd())
print(os.path.dirname)
for root  in os.walk(directory):