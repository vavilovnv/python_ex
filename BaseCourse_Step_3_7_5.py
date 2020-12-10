# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
# Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
# Файл состоит из набора строк, каждая из которых представляет собой три поля:
# Класс Фамилия Рост
#
# Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11
# включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего
# требуется вычислить значение в виде вещественного числа.
# 
# Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
# Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.

s = {i:[0, 0] for i in range(1,12)}

with open('input.txt') as f:
    for line in f:
        line = line.strip().split()
        if int(line[0]) in s:
            s[int(line[0])][0] += int(line[2])
            s[int(line[0])][1] += 1

for c, h in s.items():
    if h[0] == 0:
        print(c, '-')
    else:
        print(c, h[0]/h[1])