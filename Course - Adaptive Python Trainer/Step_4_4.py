# Текст задания: https://stepik.org/lesson/21209/step/2?adaptive=true&unit=5095

# Суть задачи та же, что и Caesar cipher, с одним отличием: кодируются символы из интервала 1F600—1F64F таблицы символов
# Юникода. Используется кодировка UTF-8.
# Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить единичный
# сдвиг, то он заменится на первый символ, и наоборот.
# Напишите программу, которая шифрует текст шифром Цезаря.
# Формат ввода:
# На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число соответствует сдвигу
# вправо. На второй строке указывается непустая фраза для шифрования.
# Не обращайте внимания, если у вас отображаются прямоугольники вместо некоторых символов. Это значит, что ваш шрифт не
# содержит этих символов. Для решения задачи это не имеет никакого значения.
# Формат вывода:
# Единственная строка, в которой записана фраза: Result: "..." , где вместо многоточия внутри кавычек записана
# зашифрованная последовательность.

a = ''.join([chr(i) for i in range(int(0x1f600), int(0x1f64f)+1)])
delta, message, count = int(input()), input().strip(), len(a)

print('Result: "', end='')
for simbol in message:
    print(a[(a.find(simbol) + delta) % count], end='')
print('"')
