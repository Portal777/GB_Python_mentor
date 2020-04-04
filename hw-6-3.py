"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.

В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить
значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income.update({"wage": wage, "bonus": bonus})

    def get_full_name(self):
        return " ".join((self.name, self.surname, self.position))

    def get_total_income(self):
        return sum(self._income.values())


first_worker = Position("Вася", "Пупкин", "Менеджер", 15000, 8000)
print(first_worker.get_full_name())
print(first_worker.get_total_income())
