# name = "Myhailo"
# city = "Bucha"
# message = "hello world"
#
# print(len(message))
#print(len()) довжина рядка
#len повиртає кількість символів
#
# print(name[0])
# print(name[-1])
# #name це перелік рядків по рахунку, останій символ завжди -1
# print(message[len(message) - 1])
# print(city[10])
#  10 це помилка по кількості символів
#text = input()
#
# if len(text) > 0:
#     print(text[0])
# else:
#     print('рядок порожній')
# text = "hello world"
# print(text[:2])
# print(text[2:])
# print(text[2:5])
# print(text[::-1])

# text[3] = "3"
# print(text)

#метод це функція яка привязана до певного елементу, в нашому випадку строка
# text = "hello world"
# text2 = text.upper() всі великі літери
# print(text.lower()) всі маленькі літери
# print(text2)
# print(text2.lower)  всі маленькі
# print(text.capitalize()) Перша велика
# print(text.title()) Кожне слове з великої

# text = "       Python     programming      "
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# login = 'admin'
# user_login = input('Enter your login username: ')
# if user_login.strip() == login:
#     print('Welcome admin')

# text = ('Python')
# for char in text:
#     print(char)
#
# password = '123qwerty123'
# # print(password.isdigit())
# digits = 0
#
# for i in password:
#     if i.isdigit():
#         digits += 1
#     if i.isalpha():
#         letters += 1
#
# print(digits)
#
# print(password.isalpha()) #тільки літери
# print(password.isdigit()) #тільки цифри
# print(password.isalnum()) #тільки з літер та цифр


# text = input("Введи речення: ").strip().lower()
# golosni = 'аеєиіїуоюя'
#
# counter_golosni = 0
# for i in text:
#     if i in golosni:
#         counter_golosni += 1
# print(counter_golosni)
#
# text = "привіт       світ"
# words = text.split()
# print(words)
#
# text_new = ' увесь '.join(words) join це ставити якиісь символи між змінимми
# print(text_new)
#
# text = ("Python is easy to learn")
# new_text = text.replace("Python", "Javascript") replace міняє змінну на іншу
# print(new_text)

# word = 'Дід '
# word_norm = word.strip().lower()
# if word_norm == word_norm[::-1]:
#     print("паліндром")
# else:
#     print("Не паліндром")
#
# text = 'hello world'
#
# print(text.find("o"))
# print(text.count('l'))

email = 'student.misha.komarov@gmail.com'
if  email.lower().endswith("gmail.com"): #.startswith
    print('у тебе гуглівська почта')

