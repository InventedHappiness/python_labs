#1
#
# import math
#
# radius = float(input("Введіть радіус круга: "))
# katet1 = float(input("Введіть перший катет: "))
# katet2 = float(input("Введіть другий катет: "))
# n_items = int(input("Введіть загальну кількість предметів (N): "))
# k_per_package = int(input("Введіть кількість предметів в одній упаковці (K): "))
#
# circle_area = math.pi * (radius ** 2)
#
# hypotenuse = math.sqrt(katet1**2 + katet2**2)
#
# packages_needed = math.ceil(n_items / k_per_package)
#
# print("--- Результат ---")
# print(f"Площа круга: {round(circle_area, 2)}")
# print(f"Гіпотенуза: {round(hypotenuse, 2)}")
# print(f"Потрібно упаковок: {packages_needed}")
#
#2
#
# import random
# import statistics
#
# print("--- Завдання 2: Статистика оцінок ---")
#
# n = int(input("Введіть кількість оцінок (N): "))
#
# if n <= 0:
#     print("Помилка! Кількість оцінок має бути додатним числом.")
# else:
#     grades = []
#     for i in range(n):
#         grades.append(random.randint(1, 12))
#
#     min_grade = min(grades
#     max_grade = max(grades)
#     mean_grade = statistics.mean(grades)
#     median_grade = statistics.median(grades)
#
#     high_grades_count = 0
#     for g in grades:
#         if 10 <= g <= 12:
#             high_grades_count += 1
#
#     print(f"Оцінки: {grades}")
#     print(f"Min: {min_grade}")
#     print(f"Max: {max_grade}")
#     print(f"Середнє: {round(mean_grade, 1)}")
#     print(f"Медіана: {median_grade}")
#     print(f"Оцінок 10-12: {high_grades_count}"
#
#1 модуль це файл з розширеням .py
#2 модуль це один файл
# бібліотека це збір модулів як одна велика бібліотека
#3 import math  імпортує весь модуль повністю
# from math import sqrt імпортує одну команду sqrt
#4 as потрібне для створення псевдоніма для функції або модуля
#5 math.ceil()  округлює завжди в більшу сторону
# math.floor() — округлює завжди в меншу сторону
#6 math.pow(a, b) — завжди повертає дробове число
# a ** b — повертає той тип даних, який виходить природно
#7 randint(A, B) — генерує випадкове ціле число у проміжку від A до B включно
# choice(список) — вибирає один випадковий елемент із готового списку
# shuffle(список) — випадковим чином перемішує елементи всередині списку
#8 Середнє арифметичне — це сума всіх чисел, поділена на їхню кількість
# Медіана — це число, яке стоїть рівно посередині відсортованого списку чисел
#