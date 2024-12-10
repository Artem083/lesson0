import os

print('Текущая директория', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая директория', os.getcwd())
# os.makedirs(r'third\fourth')
# for i in os.walk('.'):
#     print(i)
os.chdir(r'C:\Users\Ram_09-06-2020\Desktop\АРТЕМ\lesson0\7_Module')
print('Текущая директория', os.getcwd())
# print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(dirs)
# print(file)
# os.startfile(file[9])
print(os.stat(file[9]).st_size)