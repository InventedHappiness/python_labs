#1
# with open('text.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
# total_lines = len(lines)
# total_words = 0
# total_chars = 0
#
# max_len = 1
# longest_line_num = 0
# longest_line_text = ""
#
# for index, line in enumerate(lines, start=1):
#     total_words += len(line.split())
#     total_chars += len(line)
#     clean_line = line.rstrip("\n")
#     current_len = len(clean_line)
#     if current_len > max_len:
#         max_len = current_len
#         longest_line_num = index
#         longest_line_text = clean_line
#
# print(f"Рядків: {total_lines}")
# print(f"Слі: {total_words}")
# print(f"Символів: {total_chars}")
# print(f"Найдовший рядок: №{longest_line_num}, {max_len} символів")
# print(f"Текст: {longest_line_text}")
#
#
#Я файл text.txt використовував той що був в класній роботі
#
#2
#
# search_fragment = input("Фрагмент:").strip().lower()
#
# found_any = False
#
#
# with open("text.txt", "r", encoding="utf-8") as file:
#     for index, line in enumerate(file, start=1):
#         if search_fragment in line.lower():
#             clean_line = line.rstrip("\n")
#             print(f"{index}. {clean_line}")
#             found_any = True
#
# if not found_any:
#     print("Рядків з таким фрагменттм немає")
#
#Я файл text.txt використовував той що був в класній роботі

#3
#
# with open("students.txt", "w", encoding="utf-8") as file:
#     file.write("Ivanenko Anna;91\n")
#     file.write("Petrenko Ivan;76\n")
#     file.write("Komarova Olha;97\n")
#
# students = []
#
# with open("students.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         line = line.strip()
#         if not line:
#             continue
#         name, score_str = line.split(";")
#         score = int(score_str)
#         if score > 80:
#             students.append((name, score))
# students.sort(key=lambda student: student[1], reverse=True)
#
# with open("result.txt", "w", encoding="utf-8") as out_file:
#     for name, score in students:
#         out_file.write(f"{name};{score}\n")
# print("\nВміст файлу result.txt:")
# with open("result.txt", "r", encoding="utf-8") as res_file:
#     print(res_file.read().strip())

#Контрольні Запитання
#11 Файли потрібні для довготривалого збереження даних
#12 Текстовий файл складається із закодованих символів
#Бінарний (двійковий) файл містить послідовність байтів
#13 with open(...) арантує що файл автоматично закриється після завершення роботи з ним
#14r — тільки для читання. Файл повинен існувати, інакше виникне помилка.
#w — для запису. Якщо файлу немає, він створиться
#a — для дозапису. Нові дані додаються в кінець файлу
#x — для ексклюзивного створення. Створює новий файл, але якщо такий файл уже існує, програма видасть помилку
#15 Цей параметр вказує правильну таблицю кодування символів
#16 read()  зчитує весь файл повністю
# readline()  зчитує лише один  рядок файлуу
#17 Метод strip() видаляє всі пробільні символи
#
#
#