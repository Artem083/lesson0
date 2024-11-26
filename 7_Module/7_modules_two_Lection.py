from pprint import pprint

name = 'edu2.txt'
file = open(name, 'a') # режимы открытия файла: чтение, запись, добавление    # r, w, a read, write, append
file.write('\nhello world')
file.close()