# Текст задания: https://stepik.org/lesson/3363/step/2?unit=1135

# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

def is_number(x):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return x in numbers


def get_count(_s, ind):
    value = ''
    for _i in range(ind - len(_s) + 1, len(_s)):
        if is_number(_s[_i]):
            value += _s[_i]
        else:
            return int(value)


with open('test.txt', 'r') as f:
    s = f.readline().strip()

output = ''
for i in range(len(s)):
    if not is_number(s[i]):
        output += s[i] * get_count(s, i)

with open('out.txt', 'w') as f:
    f.write(output)
