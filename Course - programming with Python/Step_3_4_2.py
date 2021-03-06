# Текст задания: https://stepik.org/lesson/3363/step/3?unit=1135

# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
# слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
# лексикографически первое (можно использовать оператор < для строк).
# # В качестве ответа укажите вывод программы, а не саму программу.
# # Слова, написанные в разных регистрах, считаются одинаковыми.

d = {}
with open('test.txt', 'r') as f:
    for line in f:
        s = line.strip().lower().split()

        for word in s:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

bestword, maxcount = '', 0
for word, count in d.items():
    if count > maxcount:
        bestword, maxcount = word, count
    elif count == maxcount and word < bestword:
        bestword = word

print(bestword, maxcount)
