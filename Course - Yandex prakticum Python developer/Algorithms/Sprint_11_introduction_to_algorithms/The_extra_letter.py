"""
Лишняя буква.

Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки
s и t, состоящие только из строчных букв. Строка t получена перемешиванием
букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти
добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины строк не
превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.

Пример 1
Ввод
abcd
abcde
Вывод
e

Пример 2
Ввод
go
ogg
Вывод
g
Пример 3
Ввод
xtkpx
xkctpx
Вывод
c
"""

s, t = sorted(list(input())), sorted(list(input()))
for i in range(len(s)):
    if s[i] != t[i]:
        print(t[i])
        break
    if s[-i-1] != t[-i-1]:
        print(t[-i-1])
        break