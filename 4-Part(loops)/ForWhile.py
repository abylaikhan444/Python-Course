# .................................................................................................................................................
# from itertools import count
# from traceback import print_tb

# for i in range(5):
#     num = int(input())
#     print("Квадрат вашего числа равен:", num * num)

# print("Цикл завершен")

# .................................................................................................................................................

# for i in range(6):
#     print('AAA')

# for i in range(5):
#     print('BBBB')

# print('E')

# for i in range(9):
#     print('TTTTT')

# print('G')

# .................................................................................................................................................\

# text = input()
# n = int(input())

# for i in range(n):
#     print(text)

# .................................................................................................................................................


# n = int(input())

# for i in range(n):
#     print('*******************')

# .................................................................................................................................................


# text = input()

# for i in range(10):
#     print(i, text)


# .................................................................................................................................................

# n = int(input())

# for i in range(n + 1):
#     print("Квадрат числа", i, "равен", pow(i, 2))


# .................................................................................................................................................

# n = int(input())

# for i in range(n):
#     print((n - i) * '*')


# .................................................................................................................................................


# m = int(input())
# p = int(input())
# n = int(input())

# for day in range(1, n + 1):
#     print(day, m)
#     m = m + m * p / 100


# .................................................................................................................................................


# for i in range(10, -2, -2):
#     print(i)

# .................................................................................................................................................

# m = int(input())
# n = int(input())

# for i in range(m, n):
#     print(i)


# .................................................................................................................................................

# m = int(input())
# n = int(input())

# if m < n:
#     for i in range(m, n + 1, 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)


# .................................................................................................................................................

# m = int(input())
# n = int(input())

# if m <= n:
#     for i in range(m, n + 1):
#         if i % 2 != 0:
#             print(i)
# else:
#     for i in range(m, n - 1, -1):
#         if i % 2 != 0:
#             print(i)


# .................................................................................................................................................


# m = int(input())
# n = int(input())

# for i in range(m, n + 1):
#     if (i % 3 == 0 and i % 5 == 0) or i % 17 == 0 or i % 10 == 9:
#         print(i)

# .................................................................................................................................................


# a = int(input())

# for i in range(1, 11):
#     print(a, 'x', i, '=', a * i)


# .................................................................................................................................................

# counter = 0

# for _ in range(5):
#     scorePoini = int(input())
#     counter += scorePoini
#     print(counter)

# .................................................................................................................................................

# a = int(input())
# b = int(input())
# counter = 0

# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter = counter + 1

# print(counter)


# .................................................................................................................................................

# n = int(input())

# sum = 0

# for _ in range(n):
#     a = int(input())
#     sum = sum + a

# print(sum)


# .................................................................................................................................................


# from math import*
# counter = 0
# n = int(input())
# for i in range(1, n+1):
#     counter = counter + 1/i
# print(counter - log(n))


# .................................................................................................................................................


# n = int(input())
# counter = 0

# for i in range(1, n):
#     if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8:
#         counter += i

# print(counter)

# .................................................................................................................................................

# from math import factorial

# n = int(input())

# print(factorial(n))

# .................................................................................................................................................

# counter = 0
# n = int(input())

# for i in range (n):
#     if i % 2 == 0:
#         counter += i + 1
#     else:
#         counter -= i + 1

# print(counter)

# .................................................................................................................................................


# n = int(input())
# maxNum = 0
# maxNum2 = 1

# for i in range(n):
#     a = int(input())
#     if a > maxNum:
#         maxNum2 = maxNum
#         maxNum = a
#     elif a > maxNum2:
#         maxNum2 = a

# print(maxNum2)
# print(maxNum)


# .................................................................................................................................................

# counter = 0

# for i in range(10):
#     a = int(input())
#     if a % 2 == 0:
#         counter += 1

# if counter % 2 == 0:
#     print("YES")
# else:
#     print("NO")

# .................................................................................................................................................


# n = int(input())
# x, y = 1, 1

# for i in range(0, n):
#     x, y = y, x + y
#     print(x, end=' ')


# .................................................................................................................................................

# num = int(input())
# while num != -1:
#     print("Квадрат вашего числа равен:", num * num)
#     num = int(input())


# .................................................................................................................................................

# используем for
# for i in range(0, 100, 3):
#     print(i)

# # используем while
# i = 0
# while i < 100:
#     print(i)
#     i += 3


# .................................................................................................................................................


# text = input()
# total = 0
# while text != 'stop':
#     total += int(text)
#     text = input()

# print('Сумма чисел равна', total)


# .................................................................................................................................................

# a = True

# while a == True:
#     print('GO')


# .................................................................................................................................................


# count = 1
# while count < 10:
#     print('Python awesome!')


# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2

# print(a)


# .................................................................................................................................................

# word = input()

# while word != "КОНЕЦ":  # пока слово не равно "КОНЕЦ"
#     print(word)
#     word = input()


# .................................................................................................................................................


# while True:
#     n = int(input())
#     if n % 7 != 0:   # если число не делится на 7 → конец
#         break
#     print(n)         # иначе выводим


# .................................................................................................................................................

# sum = 0

# while True:
#     n = int(input())
#     if n < 0:
#         break
#     sum += n

# print(sum)

# .................................................................................................................................................

# count = 0

# while True:
#     mark = int(input())
#     if mark <= 0 or mark > 5:
#         break
#     elif mark == 5:
#         count += 1

# print(count)

# .................................................................................................................................................


# price = int(input())

# coins = [25, 10, 5, 1]  # номиналы монет
# count = 0               # количество монет

# for coin in coins:
#     count += price // coin   # сколько монет этого номинала берём
#     price %= coin            # остаток

# print(count)

# .................................................................................................................................................

# n = int(input())
# listNumber = []
# while n > 0:
#     last = n % 10
#     listNumber.append(last)
#     n //= 10

# print('Максимальная цифра равна', max(listNumber))
# print('Минимальная цифра равна', min(listNumber))


# .................................................................................................................................................

# num = int(input())
# resNum = num
# resNumCopy = num
# sumNum = 0
# countNum = 0
# multpleNum = 1
# firstDigit = 0

# while num != 0:
#     lastNum = num % 10
#     sumNum += lastNum
#     countNum += 1
#     multpleNum *= lastNum
#     avarage = sumNum / countNum
#     num //= 10

# while resNum != 0:
#     lastDigit = resNum % 10
#     lastDigitNum = lastDigit
#     resNum = resNum // 10

# print(sumNum)
# print(countNum)
# print(multpleNum)
# print(avarage)
# print(lastDigitNum)
# print(lastDigitNum + (resNumCopy % 10))


# num = int(input())
# resNumCopy = num

# sumNum = 0
# countNum = 0
# multNum = 1

# while num != 0:
#     lastNum = num % 10
#     sumNum += lastNum
#     countNum += 1
#     multNum *= lastNum
#     num //= 10

# average = sumNum / countNum
# lastDigit = resNumCopy % 10
# firstDigit = int(str(resNumCopy)[0])  # можно было бы и циклом

# print("Сумма цифр:", sumNum)
# print("Количество цифр:", countNum)
# print("Произведение цифр:", multNum)
# print("Среднее арифметическое:", average)
# print("Первая цифра:", firstDigit)
# print("Сумма первой и последней цифры:", firstDigit + lastDigit)


# .................................................................................................................................................


# num = int(input())

# while num != 0:
#     lastDigit = num % 10

#     if 10 < lastDigit > 99:
#         newNumber = lastDigit

#     num //= 10
# print(lastDigit)

# num = int(input())
# digits = 0
# temp = num
# while temp > 0:
#     temp //= 10
#     digits += 1
# second_digit = (num // (10 ** (digits - 2))) % 10
# print(second_digit)

# print(num // 10)


# .................................................................................................................................................

# num = int(input())
# trueCount = 0
# copyLastDigit = num % 10

# while num != 0:
#     lastDigit = num % 10
#     if lastDigit == copyLastDigit:
#         trueCount += 0
#     else:
#         trueCount += 1
#     num //= 10

# if trueCount == 0:
#     print('YES')
# else:
#     print('NO')


# .................................................................................................................................................


# num = int(input())
# prev = num % 10      # последняя цифра
# num //= 10
# ordered = True

# while num > 0:
#     current = num % 10
#     if current < prev:   # нарушение неубывания
#         ordered = False
#         break
#     prev = current
#     num //= 10

# print("YES" if ordered else "NO")

# .................................................................................................................................................


# for i in range(1, 101):
#     if i == 10 or i == 20 or i == 30 or i == 40:
#         continue
#     print(i)

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20


# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')


# for i in range(1, 10):
#     print(i)


# num = int(input())

# for i in range(2, num + 1):
#     if num % i == 0:
#         minValue = i
#         break
#     else:
#         continue

# print(minValue)


# .................................................................................................................................................

# n = int(input())

# for i in range(1, n + 1):
#     if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
#         continue
#     print(i)


# .................................................................................................................................................


# n = int(input())

# for i in range(1, n + 1):
#     if i != 1 and n % i == 0:
#         break
# print(i)


# .................................................................................................................................................# .................................................................................................................................................

# num = int(input())
# flag = True

# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False

# if num == 1:
#     print('Число равно 1')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# .................................................................................................................................................


# n = int(input())
# product = 1
# while n != 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# .................................................................................................................................................

# s = 0
# for i in range(1, 7 + 1):
#     n = int(input())
#     if n % 2 == 0:
#         s = s + n
# print(s)


# .................................................................................................................................................

# mx = -1000001
# s = 0
# for i in range(11):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x < 0 and x > mx:
#         mx = x
# if mx == -1000001: print("NO")
# else: print(s); print(mx)

# .................................................................................................................................................

# Example of clock loop

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# .................................................................................................................................................


# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()


# .................................................................................................................................................

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i, j, end='')


# .................................................................................................................................................


# a = int(input())
#
# for i in range(a):
#     for j in range(3):
#         print(a, end=' ')
#     print()

# .................................................................................................................................................


# a = int(input())
#
# for i in range(1 , a + 1):
#     for j in range(5):
#         print(i, end=" ")
#     print()


# .................................................................................................................................................

# a = int(input())
#
# for i in range(1, a // 2 + 2):
#     print('*' * i)
#
# for j in range(a // 2, 0, -1):
#     print('*' * j)


# .................................................................................................................................................

# a = int(input())
#
# for i in range(1, a + 1):
#     for j in range(i):
#         print(i, end='')
#     print()


# .................................................................................................................................................



#
# for x in range(1, 13):
#     for y in range(1, 12):
#         for z  in range(1, 11):
#             if 28 * x + 30 * y + 31 * z == 365:
#                 print(x, y, z)


# .................................................................................................................................................

# total = 0
#
# for i in range(11):          # максимум 10 быков (10*10=100)
#     for j in range(21):      # максимум 20 коров (20*5=100)
#         for k in range(201): # максимум 200 телят (200*0.5=100)
#             if i + j + k == 100 and 10*i + 5*j + 0.5*k == 100:
#                 total += 1
#                 print("Быков:", i, "Коров:", j, "Телят:", k)
# print("Всего решений:", total)

# .................................................................................................................................................

# a = int(input())
# num = 1
#
# for i in range(1, a + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

# .................................................................................................................................................

# a = int(input("Enter a number: "))
#
# for i in range(1, a + 1):
#     for j in range(i):
#         print(j + 1, end="")
#     for k in range(i - 1, 0, -1):
#         print(k, end="")
#     print()

# .................................................................................................................................................


# a = int(input())
# count = 0
#
# for i in range(1, a + 1):
#     count = 0
#     for k in range(1, i + 1):
#         if i % k == 0:
#             count += 1
#     print(i, '+' * count, sep='')


# .................................................................................................................................................

# a = int(input())
# b = int(input())
#
# big_sum = 0
# big_num = 0
#
# for num in range(a, b + 1):
#     sum_count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             sum_count += i
#     if sum_count > big_sum or (sum_count == big_sum and num > big_num):
#         big_sum = sum_count
#         big_num = num
#
# print(big_num, big_sum)



# .................................................................................................................................................


# n = int(input())
#
# while n >= 10:
#     total_n = 0
#     while n > 0:
#         total_n += n % 10
#         n //= 10
#     n = total_n
#
# print(n)

# for i in range(n):
#     last_digit = n % 10
#     total_n += last_digit
#     n //= 10
# print('First Total Sum: ', total_n)
#
# total_n2 = total_n
# for _ in range(total_n2):
#     if total_n2 < 10:
#         total_n2 = total_n
#         break
#     elif total_n > 10:
#         last_digit2 = total_n % 10
#         total_n2 += last_digit2
#         n //= 10
# print('Second Total Sum: ', total_n2)


# .................................................................................................................................................


# n = int(input())
# total = 0
#
# for j in range(1, n + 1):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     total += fact
#
# print(total)


# .................................................................................................................................................


# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)

# .................................................................................................................................................


# n = int(input())
# res = 1
# i = 2
# while i <= n:
#     res *= i
#     i += 1
# print(res)


# .................................................................................................................................................


# n = int(input())
# last_digit = 0
# all_numbers = 0
# while n > 0:
#     last_digit = n % 10
#     if last_digit % 2 == 0:
#             all_numbers += last_digit
#     n = n // 10
#
# print(all_numbers)


# .................................................................................................................................................

# n = 7
# count = 0
# maximum = None
# for i in range(n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if maximum is None or x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# .................................................................................................................................................


# n = 4
# count = 0
# maximum = 300
# for i in range(n):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# .................................................................................................................................................


# n = int(input())
# print('*' * 19)
#
# for i in range(n - 2):
#     print('*', ' ' * 15, '*')
#
# print('*' * 19)


# .................................................................................................................................................


# n = int(input())
# last_digit = 0
#
# while n >= 100:
#     last_digit = n % 10
#     n = n // 10
# print(last_digit)


# .................................................................................................................................................

# num = int(input("Enter a number: "))
# num_copy_two = num
# num_copy_three = num
# num_copy_four = num
# num_copy_five = num
# num_copy_six = num
# # количество цифр 3 в нем
# last_digit = 0
# last_digit_copy = num % 10
# counter_of_three = 0
# counter_of_last_digit = 0
# counter_of_odd = 0
#
# for i in range(num):
#     last_digit = num % 10
#     if last_digit == 3:
#         counter_of_three += 1
#     num = num // 10
# print('Количество цифр 3:', counter_of_three)
#
# # сколько раз в нём встречается последняя цифра
# for i in range(num_copy_two):
#     last_digit = num_copy_two % 10
#     if last_digit == last_digit_copy:
#         counter_of_last_digit += 1
#     num_copy_two = num_copy_two // 10
# print('сколько раз в нём встречается последняя цифра:',counter_of_last_digit)
#
# # количество чётных цифр
#
# while num_copy_three > 0:
#     last_digit_odd = num_copy_three % 10
#     if last_digit_odd % 2 == 0:
#         counter_of_odd += 1
#     num_copy_three = num_copy_three // 10
# print('количество чётных цифр:', counter_of_odd)
#
#
# # сумму его цифр, больших пяти
# counter_of_more_five = 0
#
# while num_copy_four > 0:
#     last_digit_more_five = num_copy_four % 10
#     if last_digit_more_five > 5:
#         counter_of_more_five = counter_of_more_five + last_digit_more_five
#     num_copy_four = num_copy_four // 10
# print('сумму его цифр, больших пяти', counter_of_more_five)
#
#
# # произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести её)
# counter_of_more_seven = 1
# found = False
#
# while num_copy_five > 0:
#     last_digit_more_seven = num_copy_five % 10
#     if last_digit_more_seven > 7:
#         counter_of_more_seven *= last_digit_more_seven
#         found = True
#     num_copy_five //= 10
# print(counter_of_more_seven)
#
# if not found:
#     print(1)
#
#
# # сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).
#
# counter_of_more_five_zero = 0
#
# while num_copy_six > 0:
#     last_digit_more_five_zero = num_copy_six % 10
#     if last_digit_more_five_zero == 0 or last_digit_more_five_zero == 5:
#         counter_of_more_five_zero += 1
#     num_copy_six = num_copy_six // 10
# print(counter_of_more_five_zero)























# .................................................................................................................................................


num = int(input())

# копии числа
num_copy_one = num
num_copy_two = num
num_copy_three = num
num_copy_four = num
num_copy_five = num
num_copy_six = num

# количество цифр 3 в нем
counter_of_three = 0
while num_copy_one > 0:
    last_digit = num_copy_one % 10
    if last_digit == 3:
        counter_of_three += 1
    num_copy_one //= 10
print(counter_of_three)

# сколько раз в нём встречается последняя цифра
last_digit_copy = num % 10
counter_of_last_digit = 0
while num_copy_two > 0:
    last_digit = num_copy_two % 10
    if last_digit == last_digit_copy:
        counter_of_last_digit += 1
    num_copy_two //= 10
print(counter_of_last_digit)

# количество чётных цифр
counter_of_odd = 0
while num_copy_three > 0:
    last_digit_odd = num_copy_three % 10
    if last_digit_odd % 2 == 0:
        counter_of_odd += 1
    num_copy_three //= 10
print(counter_of_odd)

# сумма его цифр, больших пяти
counter_of_more_five = 0
while num_copy_four > 0:
    last_digit_more_five = num_copy_four % 10
    if last_digit_more_five > 5:
        counter_of_more_five += last_digit_more_five
    num_copy_four //= 10
print(counter_of_more_five)

# произведение цифр, больших семи
counter_of_more_seven = 1
found = False
while num_copy_five > 0:
    last_digit_more_seven = num_copy_five % 10
    if last_digit_more_seven > 7:
        counter_of_more_seven *= last_digit_more_seven
        found = True
    num_copy_five //= 10

if not found:   # если нет цифр > 7
    print(1)
else:
    print(counter_of_more_seven)

# сколько раз в нём встречаются цифры 0 и 5 (суммарно)
counter_of_more_five_zero = 0
while num_copy_six > 0:
    last_digit_more_five_zero = num_copy_six % 10
    if last_digit_more_five_zero == 0 or last_digit_more_five_zero == 5:
        counter_of_more_five_zero += 1
    num_copy_six //= 10
print(counter_of_more_five_zero)










