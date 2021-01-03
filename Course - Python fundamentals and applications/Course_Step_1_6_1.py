# условие задачи https://stepik.org/lesson/24462/step/7?auth=login&unit=6768

# import sys

def is_ancestor(ans, cls):
    if ans in classes[cls]:
        return True
    else:
        check = False
        for i in classes[cls]:
            if i != cls:
                check = is_ancestor(ans, i)
                if check:
                    return True
        return False

classes = {}
for line in [input().strip().split() for i in range(int(input()))]:
    classes[line[0]] = [line[0]]
    if len(line) > 1:
        classes[line[0]] += line[2:]

for line in [input().strip().split() for i in range(int(input()))]:
    print('Yes' if is_ancestor(line[0], line[1]) else 'No')

# альтернативный ввод данных из файлов
#
# classes = {}
# with open('classes.txt', 'r') as f:
#     for line in f:
#         line = line.strip().split()
#         classes[line[0]] = [line[0]]
#         if len(line) > 1:
#             classes[line[0]] += line[2:]
# print(classes)
#
# with open('input.txt', 'r') as f:
#     for line in f:
#         line = line.strip().split()
#         if is_ancestor(line[0], line[1]):
#             print('Yes')
#         else:
#             print('No')
