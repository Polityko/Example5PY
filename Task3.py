# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 

import random

size = 10
a = [random.randint(1, 10) for i in range(size)]
x = set(a)
a.sort()
print(a)

el = list(filter(lambda x: x > 1, [a.count(i) for i in x]))
print(f'Количество повторяющихся: {sum(el)}')
print(f'Список: {x}')