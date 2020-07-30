"""
-Реализовать проект расчета суммарного расхода ткани на производство одежды.

Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.

К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).

-Проверить работу этих методов на реальных данных.

-Реализовать общий подсчет расхода ткани.

-Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""


# from abc import ABC, abstractmethod


class Clothes:  # (ABC):
    title = "Одежда"

    def __init__(self):
        self._calc = None

    @property
    # с @abstractmethod не работает строка 37
    def calc_fabric_consumption(self):
        return self._calc

    def __add__(self, other):
        # self.__class__.__name__ == "Coat":
        result = Clothes()
        result._calc = self._calc + other._calc
        return result

    def __str__(self):
        return f'Общий расход ткани: {self._calc:.2f}'


class Coat(Clothes):
    title = "Пальто"

    def __init__(self, param):
        self.parameter = param
        super().__init__()

    @property
    def calc_fabric_consumption(self):
        self._calc = self.parameter / (6.5 + 0.5)
        return self._calc


class Suit(Coat):
    title = "Костюм"

    @property
    def calc_fabric_consumption(self):
        self._calc = 2 * (self.parameter + 0.3)
        return self._calc


a = Clothes
my_coat = Coat(48)
my_coat_2 = Coat(52)
my_suit = Suit(183)
my_suit_2 = Suit(172)

print(my_coat.calc_fabric_consumption)
print(my_coat_2.calc_fabric_consumption)
print(my_suit.calc_fabric_consumption)
print(my_suit_2.calc_fabric_consumption)

total = my_suit + my_suit_2 + my_coat + my_coat_2
print(total)
