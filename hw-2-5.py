"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
print(my_list)

while True:
    answ = input("Введите новый элемент рейтинга (число от 1 до 9), для выхода наберите 'q': ")

    if answ.isdigit():
        answ = int(answ)

        if 1 <= answ <= 9:
            my_list.append(answ)
            my_list.sort(reverse=True)
            print("\n", my_list, "\n")

    elif answ == "q":
        break
