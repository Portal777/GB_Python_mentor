"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

initial = input("Введите результат в 'км.' за первый день: ")
result = input("Введите общий результат в 'км.' который спортсмену нужно достичь: ")

while not initial.isdigit() or not result.isdigit() or int(initial) <= 0 or int(result) <= 0:

    print("\nМожно вводить только целые положительные числа")

    initial = input("\nВведите результат в 'км.' за первый день: ")
    result = input("Введите общий результат в 'км.' который спортсмену нужно достичь: ")

while int(initial) > int(result) or int(initial) == int(result):

    print("\nНачальный результат должен быть больше и не равен желаемому")

    initial = input("\nВведите результат в 'км.' за первый день: ")
    result = input("Введите общий результат в 'км.' который спортсмену нужно достичь: ")

calc = int(initial)
count = 1

while calc < int(result):
    calc *= 1.1
    count += 1

print(f"\nНа {count}-й день спортсмен достиг результата — не менее {result} км.")
