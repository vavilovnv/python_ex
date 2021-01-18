# Текст задания: https://stepik.org/lesson/21210/step/2?adaptive=true&unit=5096

# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
# вывести получившуюся статистику.
# Программа должна выводить для каждого уникального слова число его повторений (без учёта регистра).
# Формат ввода:
# Одна строка, содержащая последовательности символов через пробел
# Формат вывода:
# Набор строк, каждая из которых содержит слово и, через пробел, число -− количество раз, которое слово использовалось
# во входной строке. Регистр слов не важен, слова в выводе не должны повторяться, порядок слов произвольный.

d = input().lower().split()
for w in set(d):
    print(w, d.count(w))


