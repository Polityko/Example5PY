# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.

import random
size = 10
a = [random.randint(1, 10) for i in range(size)]
print(a)
a = list(filter(lambda x: x > 5, a))
print(a)