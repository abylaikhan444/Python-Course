from random import *

# for i in range(5):
#     print(random.randint(1, 30))
#
#     print(random.randint(1, 30))
#
#     print(random.randint(1, 30))

# Угадайка

print('Hello, bro!> Do you want to play choice?')

def choice():
    flag = True
    choice_var = input('Please enter your answer (yes / no)').lower()
    if choice_var == 'yes':
        print('Ok, lets go to play!')
    else:
        print('Thank you for playing!')

def main():
    rand_number = randint(1, 100)
    print('Please > You can try to guess number!')
    user_num = int(input('Enter number: '))
    while user_num != rand_number:
        if