#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


import random
a = [random.randint(-30, -1) for i in range(1, 10)]
print(f'Наш массив: {a}')

min = a[0]
for i in a:
    if i < min:
        min = i
min_index = a.index(min) + 1

print(f'Максимальный отрицательный элемент = {min}')
print(f'Позиция максимального отрицательного элемента = {min_index}')



