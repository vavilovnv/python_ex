# Текст задания: https://stepik.org/lesson/334150/step/10?auth=login&unit=317559

# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и
# преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    s = ''
    for c in text:
        s += '_' + c.lower() if c.isupper() else c
    return s[1:]


print(convert_to_python_case(input()))
