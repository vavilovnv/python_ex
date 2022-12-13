"""
Странное сравнение.

Жители Алгосского архипелага придумали новый способ сравнения строк. Две
строки считаются равными, если символы одной из них можно заменить на символы
другой так, что первая строка станет точной копией второй строки. При этом
необходимо соблюдение двух условий:

Порядок вхождения символов должен быть сохранён.

Одинаковым символам первой строки должны соответствовать одинаковые символы
второй строки. Разным символам —– разные.

Например, если строка s = «abacaba», то ей будет равна строка t = «xhxixhx»,
так как все вхождения «a» заменены на «x», «b» –— на «h», а «c» –— на «i».
Если же первая строка s=«abc», а вторая t=«aaa», то строки уже не будут равны,
так как разные буквы первой строки соответствуют одинаковым буквам второй.

Формат ввода
В первой строке записана строка s, во второй –— строка t. Длины обеих строк не
превосходят 10^6. Обе строки содержат хотя бы по одному символу и состоят
только из маленьких латинских букв.

Строки могут быть разной длины.

Формат вывода
Выведите «YES», если строки равны (согласно вышеописанным правилам), и «NO» в ином случае.

Пример 1
Ввод
mxyskaoghi
qodfrgmslc
Вывод
YES

Пример 2
Ввод
agg
xdd
Вывод
YES

Пример 3
Ввод
agg
xda
Вывод
NO
"""

def сompare(s1, s2):
    if len(s1) != len(s2):
        return 'NO'
    lst1, lst2, i = [''] * 26, [''] * 26, 0
    equal = True
    while i < len(s1):
        c1 = ord(s1[i]) - 97
        c2 = ord(s2[i]) - 97
        if lst1[c1] == '' and lst2[c2] == '':
            lst1[c1], lst2[c2] = s2[i], s1[i]
        else:
            if lst1[c1] != s2[i] or lst2[c2] != s1[i]:
                equal = False
                break
        i += 1
    return 'YES' if equal else 'NO'


print(сompare(input(), input()))
