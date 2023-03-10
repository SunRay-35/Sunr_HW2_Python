# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# *Пример:*

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print('Данная программа принимает на вход натуральное число N создает последовательность значений согласно формуле (1+1/n)^n и находит их сумму.')
num = input('Введите натуральное число N: ')
res_dict = {}
if num.isdigit():
    num = int(num)
    sum = 0
    for n in range(1, num+1):
        res = round((1+1/n)**n,2)
        res_dict |= {n: res}
        sum += res
    print(f'Для числа {num} создана последовательность {res_dict} с суммой элементов {sum}')
else:
    print('Введена строка, попробуйте снова')