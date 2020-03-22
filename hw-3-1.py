"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def del_func(first: str, second: str) -> str:
    """Приводит к числу и делит переданне строчные параметры, корректно отрабатывает деление на ноль и ввод букв"""
    return "Можно вводить только числа!" if not first.isdigit() or not second.isdigit() else "На ноль делить нельзя!" \
        if second.isdigit() and int(second) == 0 else f"\nИтог деления: {int(first) / int(second)}" \
        if not int(second) == 0 and (first.isdigit() or second.isdigit()) else True


print(del_func(input("Введите делимое: "), input("Введите делить: ")))
