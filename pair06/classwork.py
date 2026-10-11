import math
from math import sqrt
from math import *
import statistics as st
import random
from datetime import datetime, date

a = 81
print(sqrt(a))

grades = [10, 7, 9, 7, 2, 11, 2]
print(f'Середній Бал: {st.mean(grades)}')
print(f'mode: {st.mode(grades)}')
print(f'mediana: {st.median(grades)}')

radius = 5
print(f'Площа круга: {round((pi * pow(radius, 2)), 2)}')

b = 2.53453
print(ceil(b))
print(floor(b))


balls = 25
items = 6
import math
print(f'Повністю заповненні коробки: {math.floor(balls / items)}')
print(f'Коробок потрібно всього: {ceil(balls / items)}')

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

print(numbers)

names = ["Ivan", "Matvey", "Maria", "Ann"]
print(random.choice(names))

print(f'Сьогодні: {datetime.now()}')