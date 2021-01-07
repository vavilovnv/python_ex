# Текст задания: https://stepik.org/lesson/24473/step/4?unit=6777

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


