import os
# name = input("Enter your name: ")


# print("Створення Файлу")
#
# with open('hello.txt', "w", encoding="utf-8") as file:
#     file.write("Аня обіцяє вчитись!\n")

#r - Режим читання, файл вже повинен існувати
#w - Режим запису, якщо файл вже існує то вміст стерається а записується все що ви написали
#a - Додає контент в кінець , якщо там був вміст він не стерається, якщо а вже створений створить новий файл
#x - створення нового файлу, якщо файл вже існує буде помилка
#
# if not os.path.exists('text.txt'):
#     with open('text.txt', 'w', encoding="utf8") as file:
#         file.write("Python - популярна мова програмування.\n")
#         file.write("Python використовується для роботи з даними.\n")
#         file.write("Файли дозволяють зберігати інформацію.\n")
#         file.write("Python вимагає практики.\n")
#         file.write("Сьогодні ми працюємо з текстовими файлами.\n")
#
#     if not os.path.exists('numbers.txt'):
#         with open('numbers.txt', 'w', encoding="utf8") as file:
#             file.write("12\n8\n25\n4\n16\n")
#
#             if not os.path.exists('students.txt'):
#                 with open('students.txt', 'w', encoding="utf8") as file:
#                     file.write("Ivanenko Anna;91\n")
#                     file.write("Leshchenko Ivan;76\n")
#                     file.write("Komarova Sophie;97\n")
#                     file.write("Bondarenko Illya;84\n")
#
#             if not os.path.exists('grades.csv'):
#                 with open('grades.csv', 'w', encoding="utf8") as file:
#                     file.write("Anna;Python;11\n")
#                     file.write("Anna;Math;10\n")
#                     file.write("Ivan;Python;6\n")
#                     file.write("Ivan;Math;10\n")
#                     file.write("Sophie;Python;11\n")
#                     file.write("Sophie;Math;12\n")
#                     file.write("Illya;Python;9\n")
#                     file.write("Illya;Math;8\n")
#
#
#
#
# with open('text.txt', 'r', encoding="utf8") as file:
#     text = file.read()
# #with автоматично закриває файл після його заврешшення його робити
# #file імя змінної файла
#
# with open('log.txt', "w", encoding="utf8") as file:
#     file.write("Перщий Запуск\n")
# with open('log.txt', "w", encoding="utf8") as file:
#     file.write("Другий Запуск, перший видалено\n")
# with open('log.txt', "a", encoding="utf8") as file:
#     file.write("Новий запис, додаємо у кінець\n")
# with open('log.txt', "r", encoding="utf8") as file:
#     print(file.read())
#
# #способи читання
# with open('text.txt', "r", encoding="utf8") as file:
#     text = file.read()
# print(f'read -> {type(text)}, count -> {len(text)}')
#
# with open('text.txt', "r", encoding="utf8") as file:
#     line1 = file.readline()#readline - наступний рядок
#     line2 = file.readline()
#     other_lines = file.readlines()#readlines створюється список усіх рядків які не було прочтиано через readline
# print(line1)
# print(line2)
# print(other_lines)
#
# with open('text.txt', "r", encoding="utf8") as file:
#     lines = file.readlines()
# print(other_lines)
# print(other_lines[0] if lines else 'Файл порожній')
#
# #перебір файлу
#
# with open('text.txt', "r", encoding="utf8") as file:
#     for number, line in enumerate(file, start=1):
#         clean_line = line.strip()
#         print(f'number -> {number}, clean_line -> {clean_line}')
#
# #розпакування
#
# line = "Ivanenko Anna;91\n"
# clean_line = line.strip()
# name, score = line.split(';')
# print(f'name -> {name}, score -> {score}')
#
#
# numbers = []
# with open('numbers.txt', "r", encoding="utf8") as file:
#     for line in file:
#         numbers.append(int(line.strip()))
# print(f'numbers -> {numbers}')
#
# students = []
# with open('students.txt', "r", encoding="utf8") as file:
#     for line in file:
#         name, score = line.strip().split(';')
#         students.append([name, int(score)])
# print(students)
#
#
# #csv
# grades = []
# with open('grades.txt', "r", encoding="utf8") as file:
#     for line in file:
#         name, subject, score = line.strip().split(';')
#         grades.append([name,subject, int(score)])
#
# t