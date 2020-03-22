"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""


def my_func() -> int:
    result = 0
    while True:
        user_input = input("Введите числа для подсчета суммы. Числа нужно разделять одним пробелом. "
                           "Для завершения - введите 'q': ")
        my_list = user_input.split(" ")

        if "q" in my_list:
            list_index = my_list.index("q")
            my_list.remove("q")
            my_list.append("q")
            if my_list == ["q"]:
                print("\nЗавершение программы")
                break
            elif False in list(map(lambda x: x.isdigit(), my_list[:list_index])):
                print("Ввод чисел произведен неверно. \nЗавершение программы")
                break
            else:
                my_list = sum((map(int, my_list[:list_index])))
                result = result + my_list
                print("Подсчет произведен. \nЗавершение программы")
                break
        elif False in list(map(lambda x: x.isdigit(), my_list)):
            print("Ввод чисел произведен неверно")
            continue
        else:
            my_list = sum(list(map(int, user_input.split(" "))))
            result = result + my_list
            print(result)
    return result


print(my_func())
