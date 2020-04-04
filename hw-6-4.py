"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.

Выполните вызов методов и также покажите результат.
"""
import random


class Car:
    speed = 0
    color = random.choice(["черный", "белый", "синий", "красный", "серебристый"])
    name = "Авто"
    is_police = False

    # go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
    def go(self):
        self.speed = random.randrange(40, 80, 10)
        return f"{self.name}: начало движение"

    def stop(self):
        self.speed = 0
        return f"{self.name}: остановилось"

    def turn(self):
        if self.speed == 0:
            return f"!{self.name}: не может повернуть, т.к. оно стоит на месте!"
        else:
            list_of_turn = ["направо", "налево", "обратно"]
            return f"{self.name}: повернуло {random.choice(list_of_turn)}"

    def show_speed(self):  # должен показывать текущую скорость автомобиля
        return f"{self.name}: скорость = {self.speed} км/ч"


class TownCar(Car):
    name = "Городское авто"
    color = random.choice(["черный", "белый", "синий", "красный", "серебристый"])

    def show_speed(self):  # При значении скорости свыше 60 - должно выводиться сообщение о превышении скорости
        if self.speed > 60:
            return f"!{self.name}: превышение допустимой скорость - 60 км/ч, на {self.speed - 60} км/ч!"
        else:
            return f"{self.name}: скорость = {self.speed} км/ч"


class SportCar(Car):
    color = random.choice(["черный", "белый", "синий", "красный", "серебристый"])
    name = "Спортивное авто"


class WorkCar(Car):
    name = "Коммерческое авто"
    color = random.choice(["черный", "белый", "синий", "красный", "серебристый"])

    def show_speed(self):  # При значении скорости свыше 60 - должно выводиться сообщение о превышении скорости
        if self.speed > 40:
            return f"!{self.name}: превышение допустимой скорость - 40 км/ч, на {self.speed - 40} км/ч!"
        else:
            return f"{self.name}: скорость = {self.speed} км/ч"


class PoliceCar(Car):
    color = "Черный"
    name = "Полицейское авто"
    is_police = True


car = Car()
print(car.name)
print(car.color)
print(car.go())
print(car.show_speed())
print(car.stop())
print(car.show_speed())
print(car.turn())
print(car.go())
print(car.turn())

print()
town_car = TownCar()
print(town_car.name)
print(town_car.color)
print(town_car.is_police)
print(town_car.go())
print(town_car.show_speed())
print(town_car.stop())
print(town_car.show_speed())
print(town_car.turn())
print(town_car.go())
print(town_car.turn())

print()
police = PoliceCar()
print(police.name)
print(police.is_police)
