"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

:>02 - длина должна составить два символа, недостающий символ заполняется "0"
"""

hours = 0
minutes = 0
seconds = 0

time = input("Введите время в секундах: ")

while not time.isdigit():
    print("\nВы ввели не число!")
    time = input("\nВведите время в секундах: ")

time = int(time)

if time > 59:
    seconds = time % 60
    minutes = time // 60 % 60
    hours = time // 60 // 60

else:
    seconds = time

print(f"\nИтог: {hours:>02}:{minutes:>02}:{seconds:>02}")
