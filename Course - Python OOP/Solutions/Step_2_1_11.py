# Условие задачи https://stepik.org/lesson/701983/step/11?unit=702084

from random import randint, choice
from string import ascii_lowercase, ascii_uppercase, digits

SIMBOLS = ascii_lowercase + ascii_uppercase + digits + '_.'


class EmailValidator:

    def __new__(cls):
        return

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        pos = email.find('@')
        if pos == -1:
            return False
        if email.count('@') > 1 or email.find('..') != -1:
            return False
        email1, email2 = email[:pos], email[pos+1:]
        return all(
            [len(email1) <= 100,
             len(email2) <= 50,
             email2.find('.') != -1,
             len(set(email1 + email2) - set(SIMBOLS)) == 0]
        )

    @classmethod
    def get_random_email(cls):
        email = ''
        email_len = randint(1, 101)
        for i in range(email_len):
            email += choice(SIMBOLS)
        return f'{email}@gmail.com'

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)
