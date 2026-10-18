# book = {
#     'title': "Кобзар"
#     'author': "Тарас Шевченко"
#     'copies': 15
# }
# print(book)
# class Book:
#     def __init__(self, title, author, copies):
#         self.title = title #куди ми записуємо
#         self.author = author #яке саме значення записуємо
#         self.copies = copies
#
#     def available(self):
#         return self.copies > 0
#
#
# book1 = Book('Кобзар', "Тарас Шевченко", 15) #self з яким обьектом пряцюємой
# # book2 = Book()
#
# print(book1.title, book1.author, book1.copies)
# print(book1.available())
#print(book2)
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
#         print(f'Rectangle width: {self.width}, height: {self.height}')
#         print(f'Perimeter: {self.perimeter()}')
#         print(f'Area: {self.area()}')
#
# rectangle = Rectangle(100, 200)
# rectangle.info()
#
#
# class Counter:
#     def __init__(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1
#
# counter1 = Counter()
# counter2 = Counter()
# print(f'Було {counter1.value, counter2.value}')
#
# counter1.increment()
# counter2.increment()
# print(f'Стало {counter1.value, counter2.value}')
#
# class Book:
#     def __init__(self, title, copies):
#         self.title = title
#         self.copies = copies
#
#     def give_one(self):
#         if self.copies > 0:
#             self.copies -= 1
#             print(f'Видано книгу {self.title}')
#         else:
#             print(f'Немає доступних примірників {self.title}')
#
#
# book = Book("Кобзар", 3)
# book.give_one()
# book.give_one()
# print(f'Залишилось', book.copies)
#
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print("Grade must be between 1 and 12")
#     def average_grade(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#     def __str__(self):
#         return f'Student {self.name}, Grades: {self.grades} Average: {self.average_grade()}'
# # student1 = Student("Anna")
# # student2 = Student("Ivan")
# # student1.grades.append(12)
# # student1.grades.append(10)
# # student2.grades.append(15)
# # print(f'Ivan: {student1.grades}, Anna: {student2.grades}')
# # print(f'Середнє: {student1.average_grade()}')
# # print(f'Середнє: {student2.average_grade()}')
#
#
#
#
#
#
# students = [
#     Student('Anna',[1, 2, 3]),
#     Student("Ivan", [12 , 10 , 11])
#
# ]
# print(f'Students: {len(students)}')
# for student in students:
#     print(f'Student: {student.name}, Grades: {student.grades}')
#
# class Product:
#     def __init__(self, name, price, count):
#         self.name = name
#         self.price = price
#         self.count = count
#     def total_price(self):
#         return self.price * self.count
# mouse = Product("Mouse", 1500, 10)
# keyboard = Product("Keyboard", 1800, 4)
#
# print(mouse.total_price())
# print(keyboard.total_price())