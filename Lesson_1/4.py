"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random
#import string

a, b = input("input range for random number: ").split()
print(random.randint(int(a), int(b)))
a, b = input("input range for random real: ").split()
print(random.uniform(float(a), float(b)))
a, b = input("input ASKII range for random char: ").split()
print(chr(random.randint(ord(a), ord(b))))
