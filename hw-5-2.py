"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

count_s = 0
count_w = 0
with open("hw-5-2-text.txt", "r") as my_file:
    for s in my_file:
        count_s += 1
        for w in s.split(" "):
            count_w += 1

print(f"Количество строк: {count_s}\nКоличество слов: {count_w}")
