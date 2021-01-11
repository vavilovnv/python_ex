# Текст задания: https://stepik.org/lesson/24469/step/6?unit=6775

s, a, b = (input() for _ in range(3))

count, impossible = 0, True
while count <= 1000:
    if a in b and a != b:
        break
    if a in s:
        s = s.replace(a, b)
        count += 1
    else:
        print(count)
        impossible = False
        break

if impossible:
    print('Impossible')