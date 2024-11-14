flag = False
for i in range(26):         # требуется сгенерировать все возм. комб-ции строч. букв англ. алфавита длиной два символа
    for j in range(26):
        text = f"{chr(ord('a')+i)}{chr(ord('a')+j)}"
        if text == "ya":   # доп. сгенер. последовательно двухбуквенные стр. по алф. до строки "YA"
            print(text)
            flag = True
            break
        print(text)
    if flag:
        break