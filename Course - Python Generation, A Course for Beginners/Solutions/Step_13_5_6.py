# Текст задания: https://stepik.org/lesson/334150/step/6?auth=login&unit=317559

# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
# возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

def is_one_away(word1, word2):
    return len(word1) == len(word2) and len([word1[i] for i in range(len(word1)) if word1[i] != word2[i]]) == 1


txt1, txt2 = input(), input()
print(is_one_away(txt1, txt2))
