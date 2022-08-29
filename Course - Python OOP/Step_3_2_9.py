# Условие задачи https://stepik.org/lesson/701987/step/9?unit=702088

class Handler:

    def __init__(self, methods=('GET', )):
        self.__methods = methods

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'

    def __call__(self, func, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            method = request.get('method', 'GET')
            if method in self.__methods:
                return self.__getattribute__(method.lower())(func, request)
            return None
        return wrapper


request = {"method": "GET", "url": "contact.html"}
@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Обработка запроса"


print(contact(request))
