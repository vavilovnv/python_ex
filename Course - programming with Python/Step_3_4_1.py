# Текст задания: https://stepik.org/lesson/3363/step/2?unit=1135

def is_number(x):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return x in numbers

def get_count(s, ind):
    value = ''
    for i in range(ind - len(s) + 1, len(s)):
        if is_number(s[i]):
            value += s[i]
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
