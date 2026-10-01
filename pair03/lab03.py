#1
#
# text = input("Введіть текст: ")
#
# total_chars = len(text)
# letters = 0
# digits = 0
# spaces = 0
# vowels_count = 0
#
# vowels = 'aeiou'
#
# for char in text:
#     if char.isalpha():
#         letters += 1
#
#         if char.lower() in vowels:
#             vowels_count += 1
#     elif char.isdigit():
#         digits += 1
#     elif char.isspace():
#         spaces += 1
#
# words = len(text.split())
#
# print(f"Символів: {total_chars}")
# print(f"літер: {letters}")
# print(f"Цифр: {digits}")
# print(f"Пробілів: {spaces}")
# print(f"Голосних: {vowels_count}")
# print(f"Слів: {words}")

#2

# raw_input = input("Введіть Прізвище, Ім'я та По батькові: ")
#
# parts = raw_input.split()
#
# if len(parts) == 3:
#     last_name = parts[0].capitalize()
#     first_name = parts[1].capitalize()
#     patronymic = parts[2].capitalize()
#
#     result = f"{last_name} {first_name[0]}.{patronymic[0]}.)"
#     print(result)
# else:
#     print("Помилка: Ви повинні ввести рівно триа слова")

#Контрольні Питання
#8.Рядок це типу послідовність символів
#9.Додатні йдуть з нуля а відємні з -1
#12.lower() робить всі букви маленькими
#capitalize() робить тільки першу літеру першого  слова великою
#title() робить всі слова з великої букви
#13.strip() для видалення пробілів в рядках
#16.isalpha() перевіряє чи рядок складається виключно з літер
#indigits() перевіряє чи рядок складається виключно з цифр
#isalnum() перевіряє чи рядок є буквено-цифровим




