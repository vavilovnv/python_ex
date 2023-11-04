# Условие задачи https://stepik.org/lesson/794582/step/15

"""
Класс Wordplay

Будем называть словом любую последовательность из одной или более латинских
букв.

Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании
экземпляра класс должен принимать один аргумент:
words — список, определяющий начальный набор слов. Если не передан, начальный
набор слов считается пустым

Экземпляр класса Wordplay должен иметь один атрибут:
words — список, содержащий набор слов

Класс Wordplay должен иметь четыре метода экземпляра:
add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в
набор. Если слово уже есть в наборе, метод ничего не должен делать
words_with_length() — метод, принимающий в качестве аргумента натуральное
число n и возвращающий список слов из набора, длина которых равна n
only() — метод, принимающий произвольное количество аргументов — букв, и
возвращающий все слова из набора, которые включают в себя только переданные
буквы
avoid() — метод, принимающий произвольное количество аргументов — букв, и
возвращающий все слова из списка words, которые не содержат ни одну из этих
букв

Примечание 1. Слова в списках, возвращаемых методами words_with_length(),
only() и avoid(), должны располагаться в том порядке, в котором они были
добавлены.

Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на
основе которого он был создан. Другими словами, если исходный список
изменится, то экземпляр класса Wordplay измениться не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными
данными.
"""

class Wordplay:
    def __init__(self, words = None):
        if not words:
            words = []
        self.words = words[::]

    def add_word(self, word):
        if not word in self.words:
            self.words.append(word)
            
    def words_with_length(self, n):
        return [i for i in self.words if len(i) == n]
    
    def only(self, *args):
        res = []
        for word in self.words:
            if all(c in args for c in list(word)):
                res.append(word)
        return res
    
    def avoid(self, *args):
        res = []
        for word in self.words:
            if not any(c in args for c in list(word)):
                res.append(word)
        return res
