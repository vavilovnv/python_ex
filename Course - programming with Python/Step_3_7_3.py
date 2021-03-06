# Текст задания: https://stepik.org/lesson/3380/step/3?unit=963

# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
# Попробуем написать подобную систему.
# На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются
# эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

s, d = set(), [input().lower() for i in range(int(input()))]
for i in range(int(input())):
    for ll in input().lower().split():
        if ll not in d:
            s.add(ll)

for ll in s:
    print(ll)
