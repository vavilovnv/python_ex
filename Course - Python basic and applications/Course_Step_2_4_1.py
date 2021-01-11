# Текст задания: https://stepik.org/lesson/24465/step/4?unit=6772

with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    f2.writelines(f1.readlines()[::-1])
