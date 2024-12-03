import io
from pprint import pprint


name = 'edu2.txt'
with  open(name, encoding ='utf-8') as file:
    for line in file:
        for char in line:
            print(line, end='')
    print(file.tell())
