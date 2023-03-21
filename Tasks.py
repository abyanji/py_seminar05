# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи


# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1 or num == 2: 
#         return 1
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)
        
# n = int(input('Введите число n: '))
# print(fibonacci(n))



# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# n = int(input('Введите число n: '))
# list_1 = [int(input('Введите оценку от 2 до 5: ')) for _ in range(n)]
# minimum = min(list_1)
# maximum = max(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == maximum:
#         list_1[i] = minimum
# print(list_1)


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def findnumber(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return print('нет')
    return print('да')

n = int(input('Введите число n: '))
findnumber(n)