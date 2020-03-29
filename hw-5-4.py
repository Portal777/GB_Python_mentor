"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import requests

# божественный гугл и прошлый опыт сдачи подобного дз
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97'
lang = 'en-ru'

line_for_write = []

with open("hw-5-4-text-1.txt", "r") as my_file:
    for line in my_file:
        word_for_translate = line.split(" ")[0]  # Разделяем строку по пробелу и берем первое слово (One,Two,Three,Four)

        # Отправляем слово на перевод в яндекс.переводчик
        result_translate = requests.post(url, data={'key': key, 'text': word_for_translate, 'lang': lang}).json()

        # Получаем данные в json-формате ({'code': 200, 'lang': 'en-ru', 'text': ['Один']}) и берем по ключу "text"
        # переведенное слово и заменяем полученную строку из открытого файла, добавляя в список, для дайнешей записи.
        result = line.replace(word_for_translate, ''.join(result_translate["text"]))
        line_for_write.append(result)

with open("hw-5-4-text-2.txt", "w") as my_file_2:
    my_file_2.writelines(line_for_write)
