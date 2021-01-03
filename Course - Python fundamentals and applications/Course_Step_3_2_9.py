# Текст задания: https://stepik.org/lesson/24470/step/15?unit=6776

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'(\w)\1+', r'\1', line)
    print(line)


