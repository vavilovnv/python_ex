# Текст задания: https://stepik.org/lesson/3380/step/3?unit=963

s, d = set(), [input().lower() for i in range(int(input()))]
for i in range(int(input())):
    for l in input().lower().split():
        if l not in d:
            s.add(l)

for l in s:
    print(l)
