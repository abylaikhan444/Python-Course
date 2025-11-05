# TASK 1
# def draw_box():
#     row = 14
#     col = 10
#
#     for i in range(row):
#         for j in range(col):
#             if i == 0 or i == row - 1:
#                 print('*', end='')
#             else:
#                 if j == 0 or j == col - 1:
#                     print('*', end='')
#                 else:
#                     print(' ', end='')
#         print()
from numpy.ma.core import count

# TASK 2
# def draw_triangle():
#     row = 10
#     for i in range(row + 1):
#         print('*' * i)
#
# draw_triangle()

# TASK 3
# name = input()
# surname = input()
# patronymic = input()
#
# def print_fio(name, surname, patronymic):
#     sum_str = surname[0] + name[0] + patronymic[0]
#     print(sum_str.upper())
#
# print_fio(name, surname, patronymic)


# TASK 4

# def print_case_counts():
#     s = input()
#     up_count = 0
#     down_count = 0
#
#     for i in s:
#         if i.isupper():
#             up_count += 1
#         elif i.islower():
#             down_count += 1
#
#     print(f'Букв в верхнем регистре: {up_count}')
#     print(f'Букв в нижнем регистре: {down_count}')
#
# print_case_counts()


# TASK 5

# объявление функции
# def print_digit_sum(num):
#     sum_count = 0
#
#     for i in range(len(n)):
#         sum_count += int(n[i])
#
#     print(sum_count)
#
# # считываем данные
# n = input()
#
# # вызываем функцию
# print_digit_sum(n)


# TASK 6

# def print_sorted_hyphen():
#     s = input().split('-')
#     words_sort = sorted(s)
#
#     for i in range(len(words_sort)):
#         result = '-'.join(words_sort[::])
#     print(result)
#
# print_sorted_hyphen()


# TASK 7

# считываем данные
# fill = input()
# base = int(input())
#
# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2):
#         print(fill * i)
#
#     for j in range(base // 2, 0, -1):
#         print(fill * j)
#
#
# # вызываем функцию
# draw_triangle(fill, base)


# TASK 8

# считываем данные
msc_time = input().split(':')

# объявление функции
def print_perm_time_call(msc_time):
    msk_hours = int(msc_time[0].replace('0', ''))
    perm_hours = str(msk_hours + 2)

    result = f'Созвон будет в {perm_hours.zfill('0')}'

    print(result)


# вызываем функцию
print_perm_time_call(msc_time)