# 1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
a = int(input("трехзначное число "))
k = a % 10
a = a // 10
l = a % 10
a = a // 10
m = a % 10
summa = k + l + m
proizv = k * l * m
print("Сумма трех чисел = " + str(summa))
print("Произведение трех чисел = " + str(proizv))
