# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')
#
#
# b = 'In 2010'
#
# print(len(b))
from numbers import Number

#
# example_word = input('Enter a word: ')
#
# for i in range(len(example_word)):
#     if i % 2 == 0:
#         print(example_word[i])

# .................................................................................................................................................


# a = input()
#
# for i in range(-1, -len(a) - 1, -1):
#     print(a[i])

# .................................................................................................................................................

# name = input("What is your name? ")
# surname = input("What is your surname? ")
# father_name = input("What is your father's name? ")
#
# print(surname[0], name[0], father_name[0], sep='')


# .................................................................................................................................................

#
# string_number = input()
# sum_int = 0
#
# for i in range(0,len(string_number)):
#     sum_int = sum_int + int(string_number[i])
# print(sum_int)


# .................................................................................................................................................


# word = input()
# count = 0
#
# for i in range(len(word)):
#     if word[i] in '0123456789':
#         count += 1
#
# if count > 0:
#     print('Цифра')
# else:
#     print('Цифр нет')


# .................................................................................................................................................

# word = input()
# multiply_count = 0
# sum_count = 0
#
# for i in range(len(word)):
#     if word[i] in '*':
#         multiply_count += 1
#     elif word[i] in '+':
#         sum_count += 1
#
# print('Символ + встречается', sum_count, 'раз')
# print('Символ * встречается', multiply_count, 'раз')


# .................................................................................................................................................

# word = input()
# count = 0
#
# for i in range(len(word) - 1):
#     if word[i] == word[i + 1]:
#         count += 1
#
# print(count)


# .................................................................................................................................................

# word = input().lower()
# count_vowels = 0
# count_spoken = 0
#
# for i in word:
#     if i in 'ауоыиэяюе':
#         count_vowels += 1
#     elif i in 'бвгджзйклмнпрстфхцчшщ':
#         count_spoken += 1
#
# print('Количество гласных букв равно',count_vowels)
# print('Количество согласных букв равно', count_spoken)


# .................................................................................................................................................


num = int(input())
reversed_num1 = ''

while num > 0:
    last = num % 2
    reversed_num1 = str(last) + reversed_num1
    num = num // 2
print(reversed_num1)
# last task




