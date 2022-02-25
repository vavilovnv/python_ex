# Текст задания: https://stepik.org/lesson/349851/step/3?unit=333706

# Переведите двоичное число в десятичную систему счисления.

def find_decimal_number(number):
    digits = '0123456789ABCDEF'
    return digits.find(number) if number in digits else 0


def calculate():
    s = 0
    for i in range(0, len(digit)):
        s += find_decimal_number(digit[i]) * (base ** (len(digit) - i - 1))
    return s


base = int(input('Введите базу для исходного числа: '))
digit = input(f'Введите число для перевода в {base}-ю систему счисления: ')
print(calculate())
