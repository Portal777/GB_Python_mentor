"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import count, cycle
from time import sleep

for i in count(777):
    print(i)
    sleep(1)

my_list = list("pizdec")

# for w in cycle(my_list):
#     print(w)
#     sleep(0.5)
#     if my_list.index(w) == len(my_list)-1:
#         sleep(1)
#         print()


