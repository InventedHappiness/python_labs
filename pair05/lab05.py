# def площа_прямокутника(width, height):
#     return width * height
#
#
# def площа_круга(radius):
#     return 3.14159 * (radius ** 2)
#
#
# def площа_трикутника(base, height):
#     return 0.5 * base * height
#
#
#
# def main():
#     print("Оберіть фігуру:")
#     print("1 — Прямокутник")
#     print("2 — Круг")
#     print("3 — Трикутник")
#
#     choice = input("Введіть номер фігури (1, 2 або 3): ")
#
#     if choice == "1":
#         w = float(input("Ширина: "))
#         h = float(input("Висота: "))
#         res = площа_прямокутника(w, h)
#         print("Площа прямокутника:", res)
#
#     elif choice == "2":
#         r = float(input("Радіус: "))
#         res = площа_круга(r)
#         print("Площа круга:", res)
#
#     elif choice == "3":
#         b = float(input("Основа: "))
#         h = float(input("Висота: "))
#         res = площа_трикутника(b, h)
#         print("Площа трикутника:", res)
#
#     else:
#         print("Неправильний вибір фігури!")
#
# main()


# def digit_sum(n):
#     total = 0
#     for char in str(n):
#         total += int(char)
#     return total
#
#
# def divisors(n):
#     result_list = []
#     for i in range(1, n + 1):
#        if n % i == 0:
#          result_list.append(i)
#     return result_list
#
#
# def is_prime(n):
#     all_divisors = divisors(n)
#     if len(all_divisors) == 2:
#      return "так"
#     else:
#         return "ні"
#
#
# def main():
#     n = int(input("N = "))
#
#     prime_status = is_prime(n)
#     divs = divisors(n)
#     d_sum = digit_sum(n)
#
#     print(f"Просте число: {prime_status}")
#     print(f"Дільники: {divs}")
#     print(f"Сума цифр: {d_sum}")

# main()

#9 Функція  це окремий імнований блок коду який виконує певну задачу
# використовоють її щоб не писати один код по сто разів
#10 Параметр  це змінна, яку ми вказуємо під час створення функції
#Аргумент — це конкретне значення або число, яке ми передаємо у функцію під час її виклику
#11 return потрібен для того  щоб завершити роботу функції та передати результт її обчислень назад у ту частину програми, яка її викликала
#12 print() просто показує текст на екрані монітора для користувача, але програма не може використовувати це значення для інших обчислень
#return віддає значення всередину програми, щоб з ним можна було працювати далі
