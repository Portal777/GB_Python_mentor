"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
numbers = [1, 2, 3, 44, 6, 23, 12]  # =91

with open("hw-5-5-text.txt", "w") as line:
    for num in numbers:
        if not num == numbers[-1]:
            line.write(str(num) + " ")
        else:
            line.write(str(num))

with open("hw-5-5-text.txt", "r") as line2:
    my_line = line2.read()
    result_list = my_line.split(" ")
    print(f"Сумма чисел: {result_list} = {sum(map(int, result_list))}")
