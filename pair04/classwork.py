#list - список , це впорядкована змінна колекція кожен елеент цієї колекції має індекс
# grades = [10, 8, 9]
# numbers = []
# numbers_new = list()
#
# grades[1] = 12
# print(grades)
#
# numbers.append(10)
# numbers.append([11, 4])
# numbers.insert(1, [5, 6,])
# numbers.extend([7, 8, 8, 9, 7, 8]) #додавання декілька елементів
# numbers.remove(7)
# numbers.pop(1)
# # numbers.clear()
# print(numbers.count(8))
# print(numbers.index(8))
#
#
# print (8 in numbers)
#
# if 8 in numbers:
#     print("True")
#
# # len()
# # min()
# # max()
# # sum()
# print(min("a", "b"))
#
# print(numbers)


# numbers = [1, 4, 6, 8, 3]
# numbers.sort(reverse = True)
# print(numbers)
#
# new_numbers = sorted(numbers)
# new_numbers.reverse()
# print(new_numbers)
#
# for number in numbers:
#     print(number)

# numbers = [1, -9, 5, -4, 34, 5, 0, -3]
# positive = []
# for number in numbers:
#     if number > 0:
#         positive.append(number)



#tuple - кортежі - незмінна колекція
# point = (-10, 12)
# rgb = (255, 0, 0)
# data = ()
# student = "Ivan", "Komarov"
# print(student)
# a = (10,)
# point = point + (30,)
# print(point)
# # print(point + a)
# point = point[:1] + point[2:]
# print(point)
# point = (-12, 6)
# x, y = point
# print(x)
# print(y)


#set - множини - не має дублікатів , не має індексного доступу, на порядок елементів у множині не звертаємо ще у множині елементи можна додавати і убирати
# subjects = {"Python", "HTML", "CSS", "JavaScript"}
# data = {}
# print(type(data))
# subjects.add("C++")
# subjects.update({"Java", "Python"})
# print(subjects)
# subjects.remove("Java")
# subjects.discard("C#")
# print(subjects)
# if "Python" in subjects:
#     print("Python")
#
#
# name = ["Ivan", "Oleg", "Olha", "Ivan", "Maria", "Maria"]
# unique_names = set(name)
# print(unique_names)
#
# group1 = {"Ivan", "Oleg", "Olha"}
# group2 = {"Ivan", "Maria", "Anna"}
#
# group3 = group1 & group2 #спільні елементи
# group4 = group1 | group2 #унікальні елементи
# group5 = group1 - group2 #знаходить елементи які є тільки в першій але нема у другій
# print(group3)
# print(group4)
# print(group5)
#

#dict - словники
# student = {
#     "name": "Ivan",
#     "grade": 11
#
# }
#
# student2 = {}
# student3 = dict()
# print(student["name"])
# student["age"] = 18
# print(student)
# student["age"] = 19
# print(student)
# student_update = student.pop("age")
# print(student_update)
# popitem = student.popitem() #видаляє останю пару значень
#
#
# student = {
#     "name": "Ivan",
#     "grade": 11
#
# }
# print(student.get("age", "Такого немає"))
# if "grade" in student:
#     print(student.get("grade"))
#
# if "Ivan" in student.values():
#     print(student.get("name"))
#
# if "Ivan" in student.keys():
#     print(student.get("name"))
#
# print(student.items())
#
#
# for key, value in student.items():
#     print(key)
#     print(value)
#
#prices = {
#    'apple': 45,
#    'banana': 70,
#    'kiwi': 70,
#    'mango': 150,
#    'orange': 100,
#
#}
#print("Усі Товари")
#for name, price in prices.items():
#    print(f"{name}: {price}грн")
#
#print("Від 50 до 100грн")
#for name, price in prices.items():
#    if price > 50 and price <= 100:
#        print(f"{name}: {price}грн")