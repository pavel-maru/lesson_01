
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1s8-oqBE4d25D68Ej_nuc3-KHhI6B5XsQ/view?usp=sharing

num = int(input('Введите трёхзначное число: '))
a = num // 100
b = (num - a * 100) // 10
c = num - a * 100 - b * 10

# print(num, a, b, c)

sum = a + b + c
mult = a * b * c

print('сумма цифр:', sum, '\nпроизведение цифр:', mult)
