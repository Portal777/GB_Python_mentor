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
from abc import ABC, abstractmethod


class Clothes(ABC):
    title = "Одежда"
    cloth_calc = 0

    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def calc_fabric_consumption(self):
        pass


class Coat(Clothes):
    title = "Пальто"

    @property
    def calc_fabric_consumption(self):
        result = self.parameter / 6.5 + 0.5
        Clothes.cloth_calc += result
        return f"Расход ткани для {self.title} = {result}"


class Suit(Clothes):
    title = "Костюм"

    @property
    def calc_fabric_consumption(self):
        result = 2 * self.parameter + 0.3
        Clothes.cloth_calc += result
        return f"Расход ткани для {self.title} = {result}"


my_coat = Coat(48)
my_coat_2 = Coat(52)
my_suit = Suit(183)
my_suit_2 = Suit(172)

print(my_coat.calc_fabric_consumption)
print(my_coat_2.calc_fabric_consumption)
print(my_suit.calc_fabric_consumption)
print(my_suit_2.calc_fabric_consumption)
print(Clothes.cloth_calc)
