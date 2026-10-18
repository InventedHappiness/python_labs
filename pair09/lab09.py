# #1
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def info(self):
#         print(f"{self.width} * {self.height}: площа = {self.area()}, периметр = {self.perimeter()}")
#
# rect1 = Rectangle(5, 3)
# rect1.info()
#
# rect2 = Rectangle(10, 4)
# rect2.info()

#2

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#         else:
#             print(f"Оцінка {grade} не додається.")
#
#     def average(self):
#         if not self.grades:
#             return 0
#         return round(sum(self.grades) / len(self.grades), 2)
#
#     def __str__(self):
#         return f"{self.name}: {self.grades}, середній = {self.average()}"
#
#
# student = Student("Ivan Pertrenko")
#
# student.add_grade(10)
# student.add_grade(12)
# student.add_grade(15)
# student.add_grade(9
#
# print(student)

#3
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#
#     def average(self):
#         if not self.grades:
#             return 0
#         return round(sum(self.grades) / len(self.grades), 2)
#
#     def __str__(self):
#         return f"{self.name} — {self.average():.2f}"
#
#
# students = [
#     Student("Anna"),
#     Student("Ivan"),
#     Student("Olha"),
#     Student("Dmytro"),
#     Student("Maria")
# ]
#
# students[0].add_grade(11); students[0].add_grade(12); students[0].add_grade(9)
# students[1].add_grade(10); students[1].add_grade(9);  students[1].add_grade(9)
# students[2].add_grade(12); students[2].add_grade(11); students[2].add_grade(11)
# students[3].add_grade(8);  students[3].add_grade(10); students[3].add_grade(7)
# students[4].add_grade(12); students[4].add_grade(11); students[4].add_grade(11)
#
# print("--- Список студентів ---")
# for student in students:
#     print(student)
#
# max_avg = max(student.average() for student in students)
#
# print("\n--- Найкращий результат ---")
# for student in students:
#     if student.average() == max_avg:
#         print(f"Найкращий результат: {student.name} — {student.average():.2f}")

#10 Клас  це креслення для створення об'єктів
#11 Об'єкт це конкретна сутність створена на основі класу
#12 Метод __init__()  це конструктор класу
#13 Параметр self  посилання на конкретний поточний об'єкт для якого викликається метод
#14 Атрибут  змінна всередині об'єкта яка збпрігає його характеристики чи дані