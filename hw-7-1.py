"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.


Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from itertools import starmap, zip_longest
from operator import add


class Matrix:

    def __init__(self, matrix_list):
        self.mtx_list = matrix_list

    def __str__(self):
        return "".join(str(self.mtx_list)).replace(",", "").replace("[", "\n").replace("]", "")

    def __add__(self, other):
        if len(self.mtx_list) < len(other.mtx_list):
            self.mtx_list = self.mtx_list + [[] for i in range(len(other.mtx_list)-len(self.mtx_list))]

        elif len(self.mtx_list) > len(other.mtx_list):
            other.mtx_list = other.mtx_list + [[] for i in range(len(self.mtx_list)-len(other.mtx_list))]

        result = list(starmap(add, zip_longest(self.mtx_list, other.mtx_list, fillvalue=0)))

        return "".join(str(result)).replace(",", "").replace("[", "\n").replace("]", "")


a = Matrix([[1123, 213, 3], [4123, 513, 633]])
b = Matrix([[1, 2, 3], [4, 51], [0, 1, 0], [132], [123, 123, 12, 3233, 3]])

print(a)
print(b)
print(a + b)
