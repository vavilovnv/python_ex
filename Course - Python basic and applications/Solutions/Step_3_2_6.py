# Текст задания: https://stepik.org/lesson/24470/step/12?unit=6776

# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'human', 'computer', line)
    print(line)
