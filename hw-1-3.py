"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369
"""

n_number = input("Введите любое целое число: ")

while not n_number.isdigit():
    print("\nВы ввели число не по условию задачи!")
    time = input("\nВведите любое целое число: ")

print(f"""\nСумма чисел по формуле {n_number} + {n_number*2} + {n_number*3} = {int(n_number) + int(n_number*2) 
                                                                             + int(n_number*3)}""")
