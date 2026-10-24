#1
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f"Ім'я: {self.name}"
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"
#
#
# student1 = Student("Anna Ivanenko", "IT-10")
#
# print(student1.info())

#2
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f"Ім'я: {self.name}"
#
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"
#
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def info(self):
#         return f"Викладач: {self.name}, предмет: {self.subject}"
#
# people_list = [
#     Person("Ivan Komarov"),
#     Student("Anna Ivanenko", "IT-10"),
#     Student("Misha Nehvorostenko", "IT-18"),
#     Teacher("Olena Kovalenko", "Python")
# ]
#
# print("--- Результат виконання циклу ---")
# for person in people_list:
#     print(person.info())

#12 Наслідування  це механізм ООП який дозволяє створювати новий клас на основі вже існуючого класу
#13 Дочірній клас записується шляхом вказання імені батьківського класу в круглих дужках після назви самого дочірнього коасу
#14 Ця конструкція використовується для виклику конструктора батьківського класу всередині конструктора дочірнього класу
#15 Перевизначення методу  створення у дочірньому класі методу з такою ж назвою та параметрами як і в батьківському класі
#16 Це можливо завдяки принципу поліморфізму в ООП