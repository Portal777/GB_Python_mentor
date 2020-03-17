"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции
"""

user_number = input("Введите целое положительное число, для нахождения большей цифры, в этом числе: ")

while not user_number.isdigit() or int(user_number) <= 0:
    print("\nВы ввели число не по условию задачи!")
    user_number = input("\nВведите целое положительное число: ")

number = int(user_number)
numeral = 0

while number != 0:
    if number % 10 == 9:
        numeral = 9
        break
    else:
        if numeral < number % 10:
            numeral = number % 10
            number //= 10
        else:
            number //= 10

print(f"Наибольшая цифра в числе {user_number}: {numeral}")
