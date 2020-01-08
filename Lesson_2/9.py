"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def Sum(n, z = 0):
    if (n < 10):
        z += n
        return int(z)
    else:
        z += int(n % 10)
        return Sum(n // 10, z)

max_sum = 0
max_int = 0
print('Подсчет суммы цифр числа и нахождение большей, для завершения введите 0')
while True:
    a = int(input('Число: '))
    if a == 0:
        break
    sum_a = Sum(a)
    if(max_sum < sum_a):
        max_sum = sum_a
        max_int = a
    print(f'Максимальная сумма {max_sum}, максимальное число {max_int}')