# Текст задания: https://stepik.org/lesson/22966/step/1?adaptive=true&unit=5367

# Напишите программу, которая проверяет, являются ли два введённых слова анаграммами.
# Программа должна вывести True в случае, если введённые слова являются анаграммами, и False в остальных случаях.
# Формат ввода:
# Два слова, каждое на отдельной строке.
# Слово может состоять только из латинских символов произвольного регистра. Регистр символов не должен влиять на ответ.

print(sorted(input().lower()) == sorted(input().lower()))










