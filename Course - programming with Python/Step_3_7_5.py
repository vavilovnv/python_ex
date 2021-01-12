# Текст задания: https://stepik.org/lesson/3380/step/5?unit=963

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