"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.


Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, mtx):
        self.matrix = mtx

    def __str__(self):
        matrix_print_text = ""
        for i in self.matrix:
            matrix_print_text = matrix_print_text + str(i) + "\n"
        return matrix_print_text

    def __add__(self, other):
        result = []
        for f_list, s_list in zip(self.matrix, other.matrix):
            my_list = []
            for f_elem, s_elem in zip(f_list, s_list):
                my_list.append(f_elem + s_elem)
            result.append(my_list)
        # result = [[g + z for g in i for z in x] for i in self.matrix for x in other.matrix]
        result_list = Matrix(result)  # лучшая строка в коде
        return result_list


a = Matrix([
    [1123, 213, 3],
    [4123, 513, 633],
    [65, 1, 77],
    [82, 22, 123]
])

b = Matrix([
    [56, 1, 99],
    [0, 58, 23],
    [98, 19, 44],
    [1, 4, 0]
])

c = Matrix([
    [113, 2, 4],
    [41, 80, 21],
    [1, 23, 62],
    [2, 22, 13]
])

print(a)
print(b)
print(c)

print(b + c)
print(a + b + c)
