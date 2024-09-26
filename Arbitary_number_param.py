# Задача "Однокоренные":
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее
# неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.
def single_root_words(root_words, *other_words):   # 1.Объявите функцию single_root_words
    # и параметры root_word и *other_words.
    same_words = []   # 2.Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    for word in other_words:   # 3. При помощи цикла for переберите предполагаемо подходящие слова.
        if root_words.lower().count(word.lower()) or word.lower().count(root_words.lower()):   # 4. Пропишите корректное
            same_words.append(word)  # относ-но задачи усл., при котором добав-ся слова в резул-ющий список same_words.
    return same_words   # 5. После цикла верните образованный функцией список same_words.


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')   # 6. Вызовите
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')   # функцию
print(result1)  # single_root_words и выведете на экран(консоль) возвращённое ей значение.
print(result2)
