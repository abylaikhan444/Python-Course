# n = int(input())
# result = list(range(1, n + 1))
#
# print(result)

# .................................................................................................................................................

#
# n = int(input())
# result = []
#
# for i in range(ord('a'), ord('a') + n):
#     result.append(chr(i))
#
# print(result)

# .................................................................................................................................................

#
# n = int(input())
# result = list(range(1, n + 1, 2))
#
# print(result)


# .................................................................................................................................................


# emoji = input()
# result = []
#
# for i in range(0, len(emoji) + 1, 2):
#     result.append(emoji[i])
#
# print(result)


# .................................................................................................................................................


# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# max_value = max(numbers)
# min_value = min(numbers)
#
# print(max_value + min_value)


# .................................................................................................................................................

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = []
# average = sum(evens) / len(evens)
#
# print(average)

# .................................................................................................................................................


# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
# for i in range(len(rainbow)):
#     if rainbow[i] == 'Green':
#         rainbow[i] = 'Зеленый'
#     elif rainbow[i] == 'Violet':
#         rainbow[i] = 'Фиолетовый'
#
#
# print(rainbow)


# .................................................................................................................................................


# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# .................................................................................................................................................

# numbers = [4, 7, -2, 1, 6]
# copy = []
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
#
# print(numbers)


# .................................................................................................................................................


# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

# last_element = numbers[len(numbers) - 1]
#
# print(len(numbers))
# print(last_element)
# print(numbers[::-1])
#
# if 5 in numbers and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
#
# del numbers[len(numbers) - 1]
# del numbers[0]
#
# print(numbers)


# .................................................................................................................................................


# n = int(input())
# words = []
#
# for i in range(n):
#     word = input()
#     words.append(word)
#
# print(words)


# .................................................................................................................................................

# word = list()
# abc = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in range(26):
#     char = chr(ord('a') + i) * (i + 1)
#     word.append(char)
#
# print(word)


# .................................................................................................................................................


# n = int(input())
# result = []
#
# for i in range(n):
#     number = int(input())
#     cube = pow(number, 3)
#     result.append(cube)
#
# print(result)



# .................................................................................................................................................


# n = int(input())
# nums = []
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         nums.append(i)
#
# print(nums)


# .................................................................................................................................................


# n = int(input())
# numbers = []
#
# # считываем все числа в список
# for _ in range(n):
#     num = int(input())
#     numbers.append(num)
#
# # создаём новый список из сумм соседних чисел
# sums = []
# for i in range(n - 1):
#     sums.append(numbers[i] + numbers[i + 1])
#
# print(sums)


# .................................................................................................................................................

# n = int(input())
# numbers = []
#
# for _ in range(n):
#     numbers.append(int(input()))
#
# result_even_index = []
#
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         result_even_index.append(numbers[i])
#
# print(result_even_index)

# .................................................................................................................................................

# n = int(input())
# words = []
# sum_words = ''
# for _ in range(n):
#     word = input()
#     words.append(word)
#
# k = int(input())
#
# for i in range(len(words)):
#     if len(words[i]) >= k:
#         sum_words += words[i][k - 1]
#     elif len(words[i]) < k:
#         continue
#
# print(sum_words)


# .................................................................................................................................................


# n = int(input())
# words = []
# redacted_words = []
# for _ in range(n):
#     word = input()
#     words.append(word)
#
# for i in range(len(words)):
#     redacted_words.extend(words[i])
#
# print(redacted_words)


# .................................................................................................................................................


# numbers = [2, 1, 1, 3, 4]
#
# total = 0
# for num in numbers:
#     if num % 2 == 1:
#         total = total + num
#
# print(total)


# .................................................................................................................................................


# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# numbers_squared = []
#
# for i in numbers:
#     numbers_squared.append(i ** 2)
#
# print(sum(numbers_squared))


# .................................................................................................................................................

# # f(x) = x**2 + 2x + 1
#
# n = int(input())
# numbers = []
#
# for _ in range(n):
#     a = int(input())
#     numbers.append(a)
# print(*numbers, sep='\n')
#
#
# print(sep="\n")
#
# for i in numbers:
#     result = i**2 + 2 * i + 1
#     print(result)
# print()


# .................................................................................................................................................


# n = int(input())
# numbers = []
#
# for i in range(n):
#     num = int(input())
#     numbers.append(num)
#
# minimum = min(numbers)
# maximum = max(numbers)
#
# del numbers[numbers.index(minimum)]
# del numbers[numbers.index(maximum)]
#
# print(*numbers, sep='\n')


# .................................................................................................................................................



# n = int(input())
# words = []
# result = []
#
# for _ in range(n):
#     word = input()
#     words.append(word)
#
# for i in words:
#     if i not in result:
#         result.append(i)
#
# print(*result, sep='\n')


# .................................................................................................................................................

# n = int(input())
# words = []
# result_sent = []
#
# for _ in range(n):
#     sentence = input()
#     words.append(sentence)
#
# word_find = input()
#
# for i in words:
#     if word_find.lower() in i.lower():
#         result_sent.append(i)
#
# print(*result_sent, sep='\n')



# .................................................................................................................................................



# n = int(input())
# words = []
# result_sent = []
#
# for _ in range(n):
#     sentence = input()
#     words.append(sentence)
#
# k = int(input())
# word_find_lst = []
#
# for _ in range(k):
#     word_find = input().lower()
#     word_find_lst.append(word_find)
#
# for i in range(len(words)):
#     lower_sentence = words[i].lower()
#     found_all = True
#
#     for j in range(len(word_find_lst)):
#         if word_find_lst[j] not in lower_sentence:
#             found_all = False
#             break
#
#     if found_all:
#         result_sent.append(words[i])
#
# print(*result_sent, sep='\n')



# .................................................................................................................................................


# n = int(input())
# numbers = []
# neg_numbers = []
# zero_numbers = []
# pos_numbers = []
#
# for _ in range(n):
#     numbers.append(int(input()))
#
# for i in range(len(numbers)):
#     if numbers[i] < 0:
#         neg_numbers.append(numbers[i])
#     elif numbers[i] == 0:
#         zero_numbers.append(numbers[i])
#     else:
#         pos_numbers.append(numbers[i])
#
# print(*neg_numbers, sep='\n')
# print(*zero_numbers, sep='\n')
# print(*pos_numbers, sep='\n')


# .................................................................................................................................................


# # print([1, 2].join())
# 
# lst = ['Мы', 'учим', 'язык', 'Python']
# lst2 = 'Мы, учим, язык, Python'
# test = lst2.split(' # ')
# 
# print(test)


# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# .................................................................................................................................................

#
# word = input()
# print(*word.split(), sep='\n')

# .................................................................................................................................................

# name = input().split()
# print(f'{name[0][0]}.{name[1][0]}.{name[2][0]}.')

# .................................................................................................................................................

# way = input()
# s = way.split('\\')
#
# print(*s, sep='\n')

# .................................................................................................................................................

# numbers = input().split(' ')
#
# for i in range(len(numbers)):
#     print('+' * int(numbers[i]))


# .................................................................................................................................................
#
# ip = input().split('.')
# count_result = 0
#
# for i in range(len(ip)):
#     if 0 <= int(ip[i]) <= 255:
#         count_result += 1
#
# if count_result == 4:
#     print('ДА')
# else:
#     print('НЕТ')


# .................................................................................................................................................

#
# words = input()
# char = input()
#
# print(char.join(words))




# .................................................................................................................................................

# numbers = input().split()
# count = 0
#
#
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             count += 1
#
# print(count)


# .................................................................................................................................................

n = [1, 2, 3]
n2 = [4, 5, 6]
n3 = [7, 8, 9]

n.append(n2)
n.append(n3)

print(n)