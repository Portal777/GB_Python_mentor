"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
сумму наибольших двух аргументов
"""


def my_func(var_1: int, var_2: int, var_3: int) -> int:
    """Принимает 3 позиционных числовых аргумента, передает в список, сортирует по значению и суммирует 2 наибольших"""
    a = [var_1, var_2, var_3]
    a.sort(reverse=True)
    return sum(a[:2])


print(my_func(2, 1, 4))
print(my_func(0, 1, 35))
