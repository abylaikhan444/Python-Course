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
import math

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

# # считываем данные
# msc_time = input().split(':')
#
# # объявление функции
# def print_perm_time_call(msc_time):
#     msk_hours = int(msc_time[0].replace('0', ''))
#     perm_hours = str(msk_hours + 2)
#
#     result = f'Созвон будет в {perm_hours.zfill(0)}:{msc_time[1]}.'
#
#     print(result)
#
#
# # вызываем функцию
# print_perm_time_call(msc_time)


# TASK 9

# word = input().lower()
# #
# #
# # def print_symbol_counts(s):
# #     # Сортируем уникальные буквы в лексикографическом порядке
# #     unique_chars = sorted(set(s))
# #
# #     for char in unique_chars:
# #         count = s.count(char)  # считаем в ИСХОДНОЙ строке
# #         print(f"{char}: {count}")
# #
# #
# # print_symbol_counts(word)


# TASK 10

# def convert_to_miles(km):
#     return km * 0.6214
#
# km = int(input())
# print(convert_to_miles(km))


# TASK 11


# def code_format(text):
#     return f'<code>{text}</code>'
#
# text = input()
# print(code_format(text))


# TASK 12

# def get_days(number_month):
#     return all_days[number_month - 1]
#
# all_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# number_month = int(input())
# print(get_days(number_month))


# TASK 13

# def get_factors(n):
#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)
#     return factors
# n = int(input())
# print(get_factors(n))


# TASK 14

# def math_round_to_int(num):
#     return math.floor(num + 0.5)
#
# num = float(input())
# print(math_round_to_int(num))


# TASK 15


# def find_all(target, symbol):
#     index_lst = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             index_lst.append(i)
#     return index_lst
#
# target = input()
# symbol = input()
# print(find_all(target, symbol))


# TASK 16


# объявление функции
def merge(list1, list2):
    pass

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))