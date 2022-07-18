# Условие задачи https://stepik.org/lesson/448983/step/8?unit=511577

# При написании собственных функций рекомендуется в комментарии описывать назначение функции, ее параметры и
# возвращаемое значение. Часто программисты откладывают написание таких комментариев напоследок, а потом и вовсе
# забывают о них 😂.
#
# На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите
# программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий. Будем считать, что
# любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит комментарий,
# если первый символ предыдущей строки - #.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.
#
# Формат выходных данных
# Программа должна вывести названия всех функций (не меняя порядка их следования в исходном файле), каждое на отдельной
# строке, для которых отсутствует поясняющий комментарий. Если все функции в файле имеют поясняющий комментарий, то
# следует вывести: Best Programming Team.

with open(input(), encoding='utf-8') as file:
    lst, functions = file.readlines(), []
    for i in range(len(lst)):
        if (i == 0 and lst[i].startswith('def')
                or lst[i].startswith('def') and not lst[i-1].startswith('#')):
            functions.append(lst[i].strip()[3:lst[i].find('(')])
    print('\n'.join(functions) if functions else 'Best Programming Team')
