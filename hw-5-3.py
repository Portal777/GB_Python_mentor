"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

employees = {}
with open("hw-5-3-text.txt", "r") as my_file:
    content = my_file.readlines()
    for i in content:
        result = i.split(" ")
        employees.update({result[0]: int(result[1].rstrip())})

empl_list = []
for key in employees:
    if employees[key] < 20000:
        empl_list.append(key)

print(f"Списко сотрудников имеющих оклад менее 20 тыс.: {empl_list}")
print(f"Средняя величина дохода всех сотрудников: {sum(employees.values())}")
