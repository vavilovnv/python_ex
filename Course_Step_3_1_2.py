# Текст задания: https://stepik.org/lesson/24469/step/7?unit=6775

s, t = (input() for i in range(2))
print(sum(1 for i in range(len(s) - len(t)+1) if s.find(t, i, i + len(t)) >= 0))