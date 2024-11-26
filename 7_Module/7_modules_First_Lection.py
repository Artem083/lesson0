# print ('hello')    # ASCII
# print (ord('h'))
# print (ord('e'))
# print (ord('l'))
# print (ord('l'))
# print (ord('o'))
#
# a = 'hello'
# chars = []
# for i in a:
#     chars.append(ord(i))
# s = ''
# for i in chars:
#     s += chr(i)
# print (s)

# for i in range(1000, 1200):
#     print (chr(i))

print(hex(ord('h')))
bb = b'\x68'
print(type(bb))
print(bb.decode())


