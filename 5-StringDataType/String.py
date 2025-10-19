# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')
#
#
# b = 'In 2010'
#
# print(len(b))
# from numbers import Number
from dataclasses import replace

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


# num = int(input())
# reversed_num1 = ''
#
# while num > 0:
#     last = num % 2
#     reversed_num1 = str(last) + reversed_num1
#     num = num // 2
# print(reversed_num1)
# # last task

# .................................................................................................................................................


# word = input()
#
# if word[::] == word[::-1]:
#     print('YES')
# else:
#     print('NO')


# .................................................................................................................................................

# word = input()
#
# #1 общее количество символов в строке
# print(len(word))
#
# #2 исходную строку, повторённую 3 раза;
# for i in range(3):
#     print(word, end='')
#
# #3 первый символ строки;
# print()
# print(word[0], end='\n')
#
# #4 первые три символа строки;
#
# print(word[0:3])
#
# #5 последние три символа строки;
#
# print(word[-3:])
#
# #6 строку в обратном порядке;
#
# print(word[::-1])
#
# #7строку с удалённым первым и последним символами.
#
# print(word[1:len(word) - 1])

# .................................................................................................................................................

# третий символ этой строки;
# предпоследний символ этой строки;
# первые пять символов этой строки;
# всю строку, кроме последних двух символов;
# все символы с чётными индексами;
# все символы с нечётными индексами;
# все символы в обратном порядке;
# все символы строки через один в обратном порядке, начиная с последнего.


# word = input()
#
# print(word[2])
#
# print(word[len(word)-2])
#
# print(word[:5])
#
# print(word[:len(word)-2])
#
# print(word[::2])
#
# print(word[1::2])
#
# print(word[::-1])
#
# print(word[::-2])

# .................................................................................................................................................


# word = input()
# left_side_word = ''
# right_side_word = ''
#
# if len(word) % 2 == 0:
#     left_side_word = word[:len(word) // 2]
#     right_side_word = word[(len(word) // 2):]
#     print(right_side_word + left_side_word)
# elif len(word) % 2 == 1:
#     left_side_word = word[:(len(word) // 2) + 1]
#     right_side_word = word[(len(word) // 2) + 1:]
#     print(right_side_word + left_side_word)


# .................................................................................................................................................

# s = ' foO BaR BAZ quX'
# print(s.capitalize())


# .................................................................................................................................................


# user_name = input()
# user_check_name = user_name.title()
#
# if user_name == user_check_name:
#     print('YES')
# else:
#     print('NO')

# .................................................................................................................................................

# word = input()
# print(word.swapcase())

# .................................................................................................................................................

#
# word = input()
# copy_word = word.lower()
#
# if 'хорош' in copy_word:
#     print('YES')
# else:
#     print('NO')

# .................................................................................................................................................

# word = input()
# count = 0
#
# for i in range(len(word)):
#     if word[i] in 'qwertyuiopasdfghjklzxcvbnm':
#         count += 1
# print(count)

# .................................................................................................................................................

# 📘 ШПОРГАЛКА ПО СТРОКОВЫМ МЕТОДАМ PYTHON

# 🔹 count(substring[, start[, end]])
# Считает, сколько раз подстрока встречается в строке.
# Пример:
# 'banana'.count('a') → 3

# 🔹 startswith(prefix[, start[, end]])
# Проверяет, начинается ли строка с указанного префикса.
# Пример:
# 'python'.startswith('py') → True

# 🔹 endswith(suffix[, start[, end]])
# Проверяет, оканчивается ли строка указанным суффиксом.
# Пример:
# 'lesson.txt'.endswith('.txt') → True

# 🔹 find(sub[, start[, end]])
# Возвращает индекс первого вхождения подстроки или -1, если не найдено.
# Пример:
# 'hello'.find('l') → 2

# 🔹 rfind(sub[, start[, end]])
# Возвращает индекс последнего вхождения подстроки или -1, если не найдено.
# Пример:
# 'hello'.rfind('l') → 3

# 🔹 index(sub[, start[, end]])
# Как find(), но вызывает ошибку ValueError, если подстрока не найдена.
# Пример:
# 'hello'.index('e') → 1

# 🔹 rindex(sub[, start[, end]])
# Как rfind(), но вызывает ошибку, если подстрока не найдена.
# Пример:
# 'hello'.rindex('l') → 3

# 🔹 strip([chars])
# Убирает пробелы (или указанные символы) с начала и конца строки.
# Пример:
# '  hi  '.strip() → 'hi'

# 🔹 lstrip([chars])
# Убирает пробелы (или указанные символы) только слева.
# Пример:
# '  hi  '.lstrip() → 'hi  '

# 🔹 rstrip([chars])
# Убирает пробелы (или указанные символы) только справа.
# Пример:
# '  hi  '.rstrip() → '  hi'

# 🔹 replace(old, new[, count])
# Заменяет подстроку old на new. Можно указать количество замен.
# Пример:
# 'banana'.replace('a', 'o') → 'bonono'


# .................................................................................................................................................


# s = input()
# word_count = s.count(' ') + 1
# print(word_count)


# .................................................................................................................................................

# word = input()
# word_in_lowercase = word.lower()
# count_Aa = 0
# count_Gg = 0
# count_Cc = 0
# count_Tt = 0
#
# for i in range(len(word_in_lowercase)):
#     if word_in_lowercase[i] == 'а':
#         count_Aa += 1
#     elif word_in_lowercase[i] == 'г':
#         count_Gg += 1
#     elif word_in_lowercase[i] == 'ц':
#         count_Cc += 1
#     elif word_in_lowercase[i] == 'т':
#         count_Tt += 1
#
# print('Аденин: ', count_Aa)
# print('Гуанин: ', count_Gg)
# print('Цитозин: ', count_Cc)
# print('Тимин: ', count_Tt)


# .................................................................................................................................................


# word = input()
# count = 0
#
# for i in word:
#     if i in '1234567890':
#         count += 1
#
# print(count)

# .................................................................................................................................................# .................................................................................................................................................

# word = input()
#
# if word.endswith('.com') or word.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# .................................................................................................................................................


# def travel_distance(avg_speed = 600, travel_time = 60):
#     KM_PER_MILE = 1.609344
#     KNOTS = 1.852
#     travel_hours = travel_time * 60
#     travel_knots = (avg_speed / KNOTS) * travel_hours
#     travel_kms = travel_knots * KNOTS
#     return travel_kms


# .................................................................................................................................................


# amount = int(input())
#
# for i in  range(amount):
#     comment = input()
#     if comment.strip() == '':
#         print(f"{i + 1}: COMMENT SHOULD BE DELETED")
#     else:
#         print(f"{i + 1}: {comment}")


# ................................................................................................................................................


# user_name = input()
#
# if (user_name.startswith('@') and
#     5 <= len(user_name) <= 15 and
#     user_name[1:].isalnum() and
#     (user_name[1:].islower() or user_name[1:].isdigit())):
#     print('Correct')
# else:
#     print('Incorrect')

# # .................................................................................................................................................
#
#
# plate = input()
#
# letters = 'АВЕКМНОРСТУХ'
#
# if (len(plate) in (9, 10) and
#     plate[0] in letters and
#     plate[1:4].isdigit() and
#     plate[4] in letters and
#     plate[5] in letters and
#     plate[6] == '_' and
#     plate[7:].isdigit()):
#     print('YES')
# else:
#     print('NO')


# .................................................................................................................................................


# print(ord(chr(65)))


# .................................................................................................................................................


# letter = input()
# next_letter = ord(letter) + 1
#
# if next_letter > 1071:
#     print('Дальше букв нет')
# elif next_letter <= 1071:
#     print(chr(next_letter))


# .................................................................................................................................................


# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     letter_code = chr(i)
#     print(letter_code, end=' ')


# .................................................................................................................................................

# sentences = input()
#
# for i in range(0, len(sentences)):
#     print(ord(sentences[i]), end=' ')


# .................................................................................................................................................


# user_first_word = input()
# user_second_word = input()
# user_third_word = input()
# user_fourth_word = input()
#
# count_first_word = 0
# count_second_word = 0
# count_third_word = 0
# count_fourth_word = 0
#
# for i in range(len(user_first_word)):
#     count_first_word += ord(user_first_word[i])
#
# for i in range(len(user_second_word)):
#     count_second_word += ord(user_second_word[i])
#
# for i in range(len(user_third_word)):
#     count_third_word += ord(user_third_word[i])
#
# for i in range(len(user_fourth_word)):
#     count_fourth_word += ord(user_fourth_word[i])
#
# max_value = max(count_first_word, count_second_word, count_third_word, count_fourth_word)
#
# if max_value == count_first_word:
#     print(user_first_word)
# elif max_value == count_second_word:
#     print(user_second_word)
# elif max_value == count_third_word:
#     print(user_third_word)
# else:
#     print(user_fourth_word)



# .................................................................................................................................................

# print(ord('🐝'))

# user_comment = input()
# coin_count = 0
#
# for i in range(len(user_comment)):
#     coin_count += ord(user_comment[i])
#
# print(f"Текст сообщения: '{user_comment}'")
# print(f"Стоимость сообщения: {coin_count * 3}🐝")



# .................................................................................................................................................


# # print(ord('🐝'))
#
# user_comment_rus = input()
# coin_count = 0
# coin_count_new = 0
# rus = 'еуорахсЕТОРАНХСВМ'
# eng = 'eyopaxcETOPAHXCBM'
#
# for i in range(len(user_comment_rus)):
#     coin_count += ord(user_comment_rus[i])
#
# for i in range(len(eng)):
#     user_comment_eng = user_comment_rus.replace(user_comment_rus[i], rus[i])
#
# for i in range(len(user_comment_eng)):
#     coin_count_new += ord(user_comment_eng[i])
#
#
# print(coin_count_new)
# print(coin_count)
#
#
# # print(f"Текст сообщения: '{user_comment_rus}'")
# # print(f"Стоимость сообщения: {coin_count * 3}🐝")


# .................................................................................................................................................

#
# number_position = int(input())
# word = input()
# word_new = ''
#
# for i in word:
#     new_char = chr((ord(i) - ord('a') - number_position) % 26 + ord('a'))
#     word_new += new_char
#
# print(word_new)


# .................................................................................................................................................

# s = input()
# for i in range(1040, 1105):
#     if str(i) in s:
#         s = s.replace(f'[u-{i}]', chr(i))
# print(s)


# .................................................................................................................................................


# first_word = input()
# second_word = input()
# third_word = input()
# fourth_word = input()
#
# min_word_length = min(first_word, second_word, third_word, fourth_word)
# max_word_length = max(first_word, second_word, third_word, fourth_word)
#
# last_letter1 = min_word_length[len(min_word_length) - 1]
# last_letter2 = max_word_length[len(max_word_length) - 1]
#
# unicode_letter1 = int(ord(last_letter1))
# unicode_letter2 = int(ord(last_letter2))
#
# multiple_two_letters = unicode_letter1 * unicode_letter2
#
# print(pow(multiple_two_letters, 2))



# .................................................................................................................................................


# word = input()
# min_word = word
# max_word = ''
#
# while word != 'КОНЕЦ':
#     word = input()
#     if word == 'КОНЕЦ':
#         break
#     if word > max_word:
#         max_word = word
#     if word < min_word:
#         min_word = word
#
# print(f'Минимальная строка ⬇️: {min_word}')
# print(f'Максимальная строка ⬆️: {max_word}')


# .................................................................................................................................................


# user_first_word = input()
# user_second_word = input()
#
# new_first = ''
# new_second = ''
#
# for i in range(len(user_first_word)):
#     if user_first_word[i].isalpha():
#         new_first += user_first_word[i]
#
# for j in range(len(user_second_word)):
#     if user_second_word[j].isalpha():
#         new_second += user_second_word[j]
#
# if new_first.lower() == new_second.lower():
#     print('YES')
# else:
#     print('NO')



# .................................................................................................................................................


# word1, word2, word3 = input(), input(), input()
#
# max_word = max(word1, word2, word3)
# min_word = min(word1, word2, word3)
#
# if word1 != max_word and word1 != min_word:
#     avg_word = word1
# elif word2 != max_word and word2 != min_word:
#     avg_word = word2
# else:
#     avg_word = word3
#
# print(min_word, avg_word, max_word)


# .................................................................................................................................................


