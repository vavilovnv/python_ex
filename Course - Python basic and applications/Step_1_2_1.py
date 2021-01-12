# Текст задания: https://stepik.org/lesson/24458/step/9?unit=6765

objects = [int(i) for i in range(100)]

ans = len(objects)
for i in range(len(objects)-1):
    for j in range(i+1, len(objects)):
        if objects[i] is objects[j]:
            ans -= 1
            break

print(ans)
