# Текст задания: https://stepik.org/lesson/3363/step/3?unit=1135

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
