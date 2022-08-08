# Условие задачи https://stepik.org/lesson/701978/step/8?unit=702079

from string import ascii_lowercase, digits

# здесь объявляйте классы TextInput и PasswordInput
class TextInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if type(name) != str or 50 < len(name) or len(name) < 3:
            raise ValueError("некорректное поле name")
        for c in name:
            if c not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if type(name) != str or 50 < len(name) or len(name) < 3:
            raise ValueError("некорректное поле name")
        for c in name:
            if c not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
