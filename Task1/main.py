# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 6782 -> 23
# 0,56 -> 11

print('Данная программа принимает на вход вещественное число и показывает сумму его цифр.')
num = input('Введите вещественное число N: ')
sum = 0
for ch in num:
    if ch.isdigit():
        sum += int(ch)
print(f'Сумма цифр в числе {num} составляет {sum}')