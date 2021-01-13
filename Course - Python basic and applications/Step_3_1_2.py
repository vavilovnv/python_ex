# Текст задания: https://stepik.org/lesson/24469/step/7?unit=6775

# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
# Пример:
# s = "abababa"
# t = "aba"
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa

s, t = (input() for i in range(2))
print(sum(1 for i in range(len(s) - len(t)+1) if s.find(t, i, i + len(t)) >= 0))
