from random import *
from sys import flags

# for i in range(5):
#     print(random.randint(1, 30))
#
#     print(random.randint(1, 30))
#
#     print(random.randint(1, 30))

# Угадайка

print('Добро пожаловать в игру "Угадайка"!')
print('Хотите сыграть? (да/нет)')

choice = input().lower()

if choice == 'да' or choice == 'yes':
    print('Отлично! Я загадал число от 1 до 100. Попробуйте угадать!')

    rand_number = randint(1, 100)
    print(f'Загаданное число! {rand_number}')
    while True:  # Бесконечный цикл
        user_num = int(input('Введите число: '))

        if user_num > rand_number:
            print('Слишком много, попробуйте еще раз')
        elif user_num < rand_number:
            print('Слишком мало, попробуйте еще раз')
        else:
            print('Вы угадали, поздравляем!')
            break  # Выходим из цикла
else:
    print('Спасибо, до встречи!')