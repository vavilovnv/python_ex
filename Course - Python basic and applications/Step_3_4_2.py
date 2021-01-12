# Текст задания: https://stepik.org/lesson/24473/step/4?unit=6777

# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
# name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от
# одного класса более одного раза. !!!*По факту наследуется*!!!
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате:
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

import json

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

data_classes = json.loads(input())

classes = {}
for eq in data_classes:
    classes[eq['name']] = eq['parents']

for c in sorted(classes.keys()):
    count = 0
    for p in classes:
        count += 1 if is_ancestor(c, p) else 0
    print(c, ':', count + 1)


