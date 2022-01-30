# Текст задания: https://stepik.org/lesson/349845/step/1?unit=333700

# программа генерирует случайное число в диапазоне от 11 до 100100 и просит пользователя угадать это число. Если догадка
# пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. Если
# догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. Если
# пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'

import random


def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


def compare(num, rand_num, count):
    if num < rand_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif num > rand_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print(f'Вы угадали c {count} попыток, поздравляем!')
        return True
    return False


def game():
    print('Укажите верхнюю границу диапазона от 1 до n:')
    rand_num, count = random.randint(1, int(input())), 0
    while True:
        count += 1
        print('Введите число:')
        num = input()
        if is_valid(num):
            if compare(int(num), rand_num, count):
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
    print('Спасибо, что играли в числовую угадайку. Еще раз? (Да/Нет)')
    while True:
        ans = input()
        if ans == 'Нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif ans == 'Да':
            game()
        else:
            print('Ответ непонятен, повторите:')


print('Добро пожаловать в числовую угадайку.')
game()
