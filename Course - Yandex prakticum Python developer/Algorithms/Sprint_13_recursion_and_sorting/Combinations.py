"""
Комбинации.

На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не
превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.

Пример 1
Ввод
23
Вывод
ad ae af bd be bf cd ce cf

Пример 2
Ввод
92
Вывод
wa wb wc xa xb xc ya yb yc za zb zc
"""

def get_combinations(s):
    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
         '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if s == '':
        return ['']
    combinations, simbols = [], d[s[-1]]
    for combination in get_combinations(s[:-1]):
        for c in simbols:
            combinations.append(combination + c)
    return combinations


print(' '.join(get_combinations(input())))
