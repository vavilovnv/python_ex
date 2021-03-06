# Текст задания: https://stepik.org/lesson/24470/step/13?unit=6776

# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово
# "argh".

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    # line = re.sub(r'a+\b', 'argh', line, count=1, flags = re.IGNORECASE)
    line = re.sub(r'([aA])+', 'argh', line, count=1)
    print(line)
