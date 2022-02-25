# Текст задания: https://stepik.org/lesson/352860/step/4?unit=336821

# требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна
# запрашивать у пользователя следующие данные:
#
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).

def make_shift(c, dct):
    delta = len(dct) if shift >= 0 else 0
    return dct[dct.find(c) + shift - delta]


def caesar_code():
    new_s = ''
    if alphabet == 'ru':
        alphabet_upper, alphabet_lower  = upper_ru, lower_ru
    else:
        alphabet_upper, alphabet_lower = upper_en, lower_en
    for c in s:
        if c in alphabet_upper:
            new_s += make_shift(c, alphabet_upper)
        elif c in alphabet_lower:
            new_s += make_shift(c, alphabet_lower)
        else:
            new_s += c
    return new_s


lower_ru, lower_en = 'абвгдежзийклмнопрстуфхцчшщъыьэюя', 'abcdefghijklmnopqrstuvwxyz'
upper_ru, upper_en = lower_ru.upper(), lower_en.upper()
s, alphabet = input('Введите строку: '), input('Укажите язык (ru/en): ')
while True:
    shift = int(input('Укажите сдвиг: '))
    print(caesar_code())
    if input('Попробуем еще раз? (yes/no)') == 'no':
        break
