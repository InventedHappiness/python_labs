#1
# input_a = input("Введіть перше число (А): ")
# input_b = input("Введіть друге число (В): ")
# operation = input("Введіть операцію (+, -, *, /): ")
#
# try:
#     a = float(input_a)
#     b = float(input_b)
#
#     if operation == '+':
#         result = a + b
#         print(f"Результат: {result}")
#     elif operation == '-':
#         result = a - b
#         print(f"Результат: {result}")
#     elif operation == '*':
#         result = a * b
#         print(f"Результат: {result}")
#     elif operation == '/':
#         if b == 0:
#             raise ZeroDivisionError("Помилка: на нуль ділити не можна")
#         result = a / b
#         print(f"Результат: {result}")
#     else:
#         print("Помилка: невідома операція")
#
# except ValueError:
#     print("Помилка: введено нечислове значення. Будь ласка, вводьте лише числв")
# except ZeroDivisionError as e:
#     print(e)

#2
#
# def input_grade():
#     while True:
#         user_input = input("Оцінка: ")
#         try:
#             grade = int(user_input)
#
#             if grade < 1 or grade > 12:
#                 raise ValueError("Помилка: оцінка повинна бути від 1 до 12.")
#
#             print(f"Прийнято: {grade}")
#             return grade
#
#
#         except ValueError as e:
#
#             if "оцінка повинна бути від 1 до 12" not in str(e):
#                 print("Помилка: потрібно ввести ціле число.")
#             else:
#                 print(e)
# input_grade()

#3
#
# students = ["Іван", "Марія", "Олександр", "Олена", "Дмитро"]
# grades = {"Математика": 11, "Фізика": 10, "Історія": 12, "Хімія": 9}
#
# print("Оберіть тип пошуку:")
# print("1 — учень за індексом")
# print("2 — оцінка за назвою предмета(пишіть будь ласка з великої літери)")
#
# choice = input("1 - учень, 2 - предмет: ").strip()
#
# if choice == "1":
#     try:
#         index_input = input("Індекс: ").strip()
#         index = int(index_input)
#
#         student = students[index]
#         print(f"Результат: Знайдено учня — {student}")
#
#     except ValueError:
#         print("Помилка: Введено нкчисловий індекс. Очікується ціле число")
#     except IndexError:
#         print("Помилка: учня з таким індексом немає")
#
# elif choice == "2":
#     try:
#         subject = input("Назва предмета: ").strip()
#
#         grade = grades[subject]
#         print(f"Результат: Оцінка з предмета '{subject}' — {grade}")
#
#     except KeyError:
#         print(f"Помилка: Предмета '{subject}' немає у словнику")
#
# else:
#     print(f"Помилка: Невідомий пункт меню '{choice}'. Будь ласка, оберіть 1 або 2.")
#11 Синтаксична помилка  виникає на етапі аналізу коду
#Виняток виникає вже під час роботи синтаксично коректної програми
#12 Вона використовується для обробки помилок (винятків) під час виконання програми
#13 Цей виняток виникає, коли функція отримує аргумент правильного типу, але з некоректним значенням
#14 Коли програма намагається виконати операцію ділення або ділення за модулем (%) на нуль
#15 IndexError виникає під час роботи з послідовностями
#16 Коли програма намагається відкрити, прочитати або видалити файл за вказаним шляхом, але цього файлу не існує на диску
#17 Щоб розділити обробку різних типів помилок
#18 Блок else виконується лише тоді, коли код у блоці try відпрацював успішно і жодного винятку не виникло



