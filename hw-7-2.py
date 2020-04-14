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


def total_consumption(first, second):
    # if isinstance(first, Coat): - ненужная проверка на принадлежность к классу (для знания)
    print(f"Общий расход ткани: {round(first.fabric_consumption + second.fabric_consumption, 2)}")


class Clothes(ABC):
    title = "Одежда"

    def __init__(self):
        pass

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    title = "Пальто"

    def __init__(self, V):
        super().__init__()
        self.V = V

    @property
    def fabric_consumption(self):
        return round(self.V / 6.5 + 0.5, 2)


class Suit(Clothes):
    title = "Костюм"

    def __init__(self, H):
        super().__init__()
        self.H = H

    @property
    def fabric_consumption(self):
        return round(2 * self.H + 0.3, 2)


some = Clothes
print(some.title)

coat = Coat(48)
print(coat.fabric_consumption)

suit = Suit(183)
print(suit.fabric_consumption)

print(coat.title)
print(suit.title)

total_consumption(coat, suit)
