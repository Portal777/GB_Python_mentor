"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def my_func(var_1: int, var_2: int) -> int:
    return var_1*var_2


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)
print(reduce(my_func, my_list))

