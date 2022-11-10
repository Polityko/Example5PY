# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.


import random

size = 10
a = [random.randint(1, 50) for i in range(size)]
print(a)

i = random.randint(0, size-1)
res = [a[i]]

while i < size:
    i = random.randint(i+1, size)
    if i < size:
        if a[i] > res[-1]:
            res.append(a[i])
print(res)

