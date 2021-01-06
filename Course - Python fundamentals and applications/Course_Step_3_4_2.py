# Текст задания: https://stepik.org/lesson/24473/step/4?unit=6777

import json

def count_children(ans, cls):
    if ans in classes[cls]:
        return 1
    else:
        check = 0
        for i in classes[cls]:
            if i != cls:
                check = count_children(ans, i)
                if check == 1:
                    return 1
        return 0

str_classes = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
data_classes = json.loads(str_classes) # input()

classes = {}
for eq in data_classes:
    classes[eq['name']] = eq['parents']
    classes[eq['name']] += eq['name']

for cls in classes:
    print(cls, ':', count_children(, cls))


