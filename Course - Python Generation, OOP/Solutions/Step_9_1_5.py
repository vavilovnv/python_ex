# Условие задачи https://stepik.org/lesson/864077/step/5

"""
Классы Domain и DomainException

Реализуйте класс исключений DomainException. Также реализуйте класс Domain для
работы с доменами. Класс Domain должен поддерживать три способа создания
своего экземпляра: напрямую через вызов класса, а также с помощью двух методов
класса from_url() и from_email():

# непосредственно на основе домена
domain1 = Domain('pygen.ru')    
# на основе url-адреса                   
domain2 = Domain.from_url('https://pygen.ru')      
# на основе адреса электронной почты
domain3 = Domain.from_email('support@pygen.ru')    
При попытке создания экземпляра класса Domain на основе некорректных домена,
url-адреса или адреса электронной почты должно быть возбуждено исключение
DomainException с текстом:
Недопустимый домен, url или email

В качестве неформального строкового представления экземпляр класса Domain
должен иметь собственный домен:

print(str(domain1))                                # pygen.ru
print(str(domain2))                                # pygen.ru
print(str(domain3))                                # pygen.ru
Примечание 1. Будем считать домен корректным, если он представляет собой
последовательность из одной или более латинских букв, за которой следует
точка, а затем снова одна или более латинских букв.

Примечание 2. Будем считать url-адрес корректным, если он представляет собой
строку http:// или https://, за которой следует корректный домен. 

Примечание 3. Будем считать адрес электронной почты корректным, если он
представляет собой последовательность из одной или более латинских букв, за
которой следует собачка (@), а затем корректный домен.
"""

from re import fullmatch, search

class DomainException(Exception):
    pass

class Domain:

    def __init__(self, url, source="domain"):
        if source == "url":
            self._check_url(url)
        elif source == "email":
            self._check_email(url)
        else:
            self._check_domain(url)
        self.url = url

    def __str__(self):
        match = search("\w+\.\w+", self.url)
        return match.group()

    @classmethod
    def from_url(cls, url):
        return Domain(url, "url")

    @classmethod
    def from_email(cls, url):
        return Domain(url, "email")

    def _check_domain(self, url):
        if not fullmatch("[a-zA-Z]+\.[a-zA-Z]+", url):
            raise DomainException("Недопустимый домен, url или email")

    def _check_url(self, url):
        if not fullmatch("https?:\/\/[a-zA-Z]+\.[a-zA-Z]+", url):
            raise DomainException("Недопустимый домен, url или email")

    def _check_email(self, url):
        if not fullmatch("[a-zA-Z]+@\w+\.\w+", url):
            raise DomainException("Недопустимый домен, url или email")
