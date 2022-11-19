# Условие задачи https://stepik.org/lesson/702004/step/5?unit=702105

class ValidatorString:

    def __init__(self, min_length, max_length, chars):
        self._min_length = min_length
        self._max_length = max_length
        self._chars = chars

    def is_valid(self, string):
        if not(isinstance(string, str)
               and self._min_length <= len(string) <= self._max_length):
            raise ValueError('недопустимая строка')
        if (len(self._chars) > 0
                and not any(s in self._chars for s in string)):
            raise ValueError('недопустимая строка')
        return string


class LoginForm:

    def __init__(self, login_validator, password_validator):
        self._login_validator = login_validator
        self._password_validator = password_validator
        self._login, self._password = None, None

    def form(self, request):
        login = request.get('login')
        password = request.get('password')
        if not login or not password:
            raise TypeError('в запросе отсутствует логин или пароль')
        self._login = self._login_validator.is_valid(login)
        self._password = self._password_validator.is_valid(password)


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
