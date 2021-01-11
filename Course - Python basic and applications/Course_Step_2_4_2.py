# Текст задания: https://stepik.org/lesson/24465/step/6?unit=6772

import os

sp = []
for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if file[-3:] == '.py':
            sp.append(current_dir)
            break
with open('output.txt', 'w') as f:
    f.writelines('\n'.join(sorted(sp)))