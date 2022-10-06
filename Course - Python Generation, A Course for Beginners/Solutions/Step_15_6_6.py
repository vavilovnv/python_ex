# Текст задания: https://stepik.org/lesson/349851/step/6?unit=333706

# Перевод чисел из десятичной системы счисления в любую другую

def find_number(n):
    dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
            9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    return dict[n]


def calculate(number):
    s = ''
    while number >= base:
        s += find_number(number % base)
        number = number // base
    s += find_number(number)
    return s[::-1]


base = int(input('Введите базу для перевода в систему счисления: '))
digit = int(input(f'Введите десятичное число для перевода в {base}-ю систему счисления: '))
print(calculate(digit))
