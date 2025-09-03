# a, b = float(input()), float(input())

# s_formula = 0.5 * a * b

# print(s_formula)


# .................................................................................................................................................


# s, v1, v2 = float(input()), float(input()), float(input())

# formula = (s / (v1 + v2))

# print(formula)


# .................................................................................................................................................

# a = float(input())

# if a // 1 == 0:
#     print("Обратного числа не существует")
# else:
#     print(pow(float(a), -1))


# .................................................................................................................................................

# a = float(input())

# celc = (5 / 9) * (a - 32)

# print(celc)


# .................................................................................................................................................

# dogAge = int(input())

# if dogAge == 1:
#     print(10.5)
# elif dogAge == 2:
#     print(21)
# elif dogAge != 1 and dogAge != 2:
#     print(21 + ((dogAge - 2) * 4))


# .................................................................................................................................................


# a = float(input())

# print(int(float((a * 10) % 10) // 1))


# .................................................................................................................................................


# a1= int(input())
# a2 = int(input())
# a3 = int(input())
# a4 = int(input())
# a5 = int(input())

# minNum = min(a1, a2, a3, a4, a5)
# maxNum = max(a1, a2, a3, a4, a5)

# print('Наименьшее число =', minNum)
# print('Наибольшее число =', maxNum)


# .................................................................................................................................................


# a1 = int(input())
# a2 = int(input())
# a3 = int(input())

# sumA = a1 + a2 + a3
# aMin = min(a1, a2, a3)
# aMax = max(a1, a2, a3)
# X = min(a1, a2, a3) + max(a1, a2, a3)
# avarageA = sumA - X

# print(aMax, avarageA, aMin, sep='\n')


# .................................................................................................................................................

# num = int(input())

# x1 = num % 10
# x2 = (num // 10) % 10
# x3 = num // 100

# maxNum = max(x1, x2, x3)
# minNum = min(x1, x2, x3)
# avarageX = (x1 + x2 + x3) - (minNum + maxNum)

# if (maxNum - minNum) == avarageX:
#     print('Число интересное')
# else:
#     print('Число неинтересное')


# .................................................................................................................................................


# a1 = abs(float(input()))
# a2 = abs(float(input()))
# a3 = abs(float(input()))
# a4 = abs(float(input()))
# a5 = abs(float(input()))


# print(a1 + a2 + a3 + a4 + a5)


# .................................................................................................................................................


# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())

# formula = abs(a1 - b1) + abs(a2 - b2)


# print(formula)


# .................................................................................................................................................


# a = '"Python is a great language!"'
# a2 = ", said Fred. "
# a3 = '"I '
# a4 = "don't"
# a5 = ' ever remember having this much fun before."'


# print(a + a2 + a3 + a4 + a5)


# .................................................................................................................................................


# name = input()
# suename = input()


# print('Hello ' + name + ' ' + suename + '!' + ' You have just delved into Python')


# .................................................................................................................................................


# clubTag = input()
# lenghtClub = str(len(clubTag))

# print("Футбольная командa " + clubTag + " имеет длину " + lenghtClub + " символов")


# .................................................................................................................................................\


# city1 = input()
# city2 = input()
# city3 = input()

# lenFirstCity = len(city1)
# lenSecondCity = len(city2)
# lenThirdCity = len(city3)

# maxCity = max(lenFirstCity, lenSecondCity, lenThirdCity)
# minCity = min(lenFirstCity, lenSecondCity, lenThirdCity)

# if lenFirstCity == maxCity:
#     maxCity = city1
# elif lenSecondCity == maxCity:
#     maxCity = city2
# else:
#     maxCity = city3


# if lenFirstCity == minCity:
#     minCity = city1
# elif lenSecondCity == minCity:
#     minCity = city2
# else:
#     minCity = city3


# print(minCity)
# print(maxCity)

# .................................................................................................................................................


# x1 = input()
# x2 = input()
# x3 = input()

# lenghtX1 = len(x1)
# lenghtX2 = len(x2)
# lenghtX3 = len(x3)

# maxLen = max(lenghtX1, lenghtX2, lenghtX3)
# minLen = min(lenghtX1, lenghtX2, lenghtX3)
# averege = (lenghtX1 + lenghtX2 + lenghtX3) - (maxLen + minLen)
# stepD = minLen - averege

# if maxLen - averege == averege - minLen:
#     print('YES')
# else:
#     print('NO')

# .................................................................................................................................................


# text = input()

# if 'синий' in text:
#     print('YES')
# else:
#     print('NO')


# .................................................................................................................................................


# text = input()

# if 'суббота' in text:
#     print('YES')
# elif 'воскресенье' in text:
#     print('YES')
# else:
#     print('NO')


# .................................................................................................................................................


# email = input()

# if '.' in email and '@' in email:
#     print('YES')
# else:
#     print('NO')

# .................................................................................................................................................
# from math import sqrt

# a1 = float(input())
# b1 = float(input())
# a2 = float(input())
# b2 = float(input())


# formula = sqrt((pow(a1 - a2, 2) + pow(b1- b2, 2)))

# print(formula)


# .................................................................................................................................................

# from math import *

# radius = float(input())

# S = pi * pow(radius, 2)
# C = 2 * pi * radius

# print(S)
# print(C)

# .................................................................................................................................................


# from math import *

# a = float(input())
# b = float(input())

# formula1 = (a + b) / 2
# formula2 = sqrt(a * b)
# formula3 = (2 * a * b) / (a + b)
# formula4 = sqrt((pow(a, 2) + pow(b, 2)) / 2)

# print(formula1, formula2, formula3, formula4, sep='\n')

# .................................................................................................................................................

# from math import *

# a = float(input())
# aRadians = radians(a)
# print(sin(aRadians) + cos(aRadians) + pow(tan(aRadians), 2))

# .................................................................................................................................................

# from math import floor, ceil

# a = float(input())

# upA = ceil(a)
# downA = floor(a)

# print(upA + downA)


# .................................................................................................................................................

# from math import *

# a = float(input())
# b = float(input())
# c = float(input())

# D = pow(b, 2) - 4 * a * c

# if D < 0:
#     print("Нет корней")
# elif D == 0:
#     x = -b / (2 * a)
#     print(x)
# else:
#     x1 = (-b - sqrt(D)) / (2 * a)
#     x2 = (-b + sqrt(D)) / (2 * a)
#     if x1 > x2:
#         print(x2)
#         print(x1)
#     else:
#         print(x1)
#         print(x2)

# .................................................................................................................................................

# from math import *

# n = int(input())
# a = float(input())

# S = (n * a**2) / (4 * tan(pi / n))
# print(S)

# .................................................................................................................................................

