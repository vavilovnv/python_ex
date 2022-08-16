# Условие задачи https://stepik.org/lesson/701985/step/8?unit=702086

class ValidateString:

    def __init__(self, min_length=0, max_length=0):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return (isinstance(string, str)
                and self.min_length <= len(string) <= self.max_length)


class StringValue:

    def __init__(self, validator: ValidateString):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not self.validator.validate(value):
            raise Exception(f"Неверное значение для {self.name}")
        setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(ValidateString(3, 100))
    password = StringValue(ValidateString(3, 100))
    email = StringValue(ValidateString(3, 100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print((f'<form>\nЛогин: {self.login}\nПароль: {self.password}'
               f'\nEmail: {self.email}\n</form>'))
