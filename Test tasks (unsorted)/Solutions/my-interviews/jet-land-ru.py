"""
1. Какие вы видите проблемы в следующем фрагменте кода? Как его следует
исправить? Исправьте ошибку и перепишите код ниже с использованием типизации.

def create_handlers(callback):
   handlers = []
   for step in range(5):
      # добавляем обработчики для каждого шага (от 0 до 4)
      handlers.append(lambda: callback(step))
   return handlers

def execute_handlers(handlers):
  # запускаем добавленные обработчики (шаги от 0 до 4)
  for handler in handlers:
     handler()
"""

"""
Ответ

Проблема в том, что в первоначальной реализации в execute_handlers()
при итерации по списку обработчиков будет вызван callable-объект handler
с одним и тем же аргументом равным последнему значению (4) переменной 
step при итерации. Так происходит потому что в create_handlers выполняется
итерация, в процессе которой в список помещаются ссылки на объекты функции 
lambda, а не результаты их исполнения. Соответственно, когда они будут вызваны
на исполнение при итерации по списку в execute_handlers в степ будет указатель
на четверку, как последнее значение при итерации по range(5). Чтобы избежать
такого поведения - можно использовать замыкание, передавая анонимной функции
при её добавлении в список параметр равный текущему значению step при
итерации.

upd. Решение оценили в 0.75 баллов, видимо что-то не учел.
"""

from typing import Any, Callable


def create_handlers(
    callback: Callable[[int], Any]
) -> list[Callable[[], Callable]]:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda x=step: callback(x))
    return handlers


def execute_handlers(handlers: list[Callable[[], Callable]]) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()


"""
2. Дано: список dict-объектов вида вида {«key»: «value»}, например 
[{«key1»: «value1»}, {«k1»: «v1», «k2»: «v2», «k3»: «v3»}, {}, {},
{«key1»: «value1»}, {«key1»: «value1»}, {«key2»: «value2»}].
Напишите функцию, которая удаляет дубликаты из этого списка. Для примера выше
возвращаемое значение может быть равно [{«key1»: «value1»}, 
{«k1»: «v1», «k2»: «v2», «k3»: «v3»}, {}, {«key2»: «value2»}].
Обязательное условие: функция не должна иметь сложность O(n^2).

upd. Решение оценили в 0 баллов и поделом. Надо было читать задачу внимательно
и учесть обязательное условие, а не козырять однострочным решением. Второе
решение - переделанное на O(n).
"""

def remove_duplicates(lst: list[dict]) -> list[dict]:
    return [d for i, d in enumerate(lst) if d not in lst[i + 1:]]


def remove_duplicates(lst: list[dict]) -> list[dict]:
    seek, n, i = set(), len(lst), 0
    while i < n:
        value = tuple(lst[i])
        if value not in seek:
            seek.add(value)
            i += 1
        else:
            lst.pop(i)
            n -= 1
    return lst


"""
3. Сколько HTML-тегов в коде главной страницы сайта jetlend.ru?
Сколько из них содержит атрибуты?

Напишите скрипт на Python, который выводит ответы на вопросы выше.

upd. Решение оценили в 1 балл.
"""

import requests
from dataclasses import dataclass

from bs4 import BeautifulSoup

TARGET_URL = 'https://jetlend.ru/'


@dataclass
class Result:
    tags: int
    attrs: int


def count_tags_and_attrs() -> Result | None:
    response = requests.get(TARGET_URL)
    if response.status_code != 200:
        return None
    # need to install the dependency: pip install lxml
    bs = BeautifulSoup(response.text, features='lxml')
    return Result(len(bs()), sum([1 for tag in bs() if tag.attrs]))


def main():
    result = count_tags_and_attrs()
    if result:
        print(f'HTML-тегов в коде страницы {TARGET_URL} - {result.tags}.')
        print(f'Среди них с атрибутами: {result.attrs}.')


if __name__ == "__main__":
    main()


"""
4. Ниже приведена схема базы данных. Borrower — заемщик, Loan — заём.

Для схемы базы данных, приведенной ниже, напишите следующие запросы с
использованием Django ORM:

Число заемщиков, имеющих закрытые займы (status = closed).
Число заемщиков, для которых существует хотя бы один заем, созданный в 2022
году.
Совокупный объем (amount) всех активных займов (status = active),
принадлежащим заемщикам, которые зарегистрировались в 2021 году.

class Borrower(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=127, default='')

class Loan(models.Model):
	STATUS_CHOICES = [
		(0, 'new'),
		(1, 'active'),
		(2, 'closed'),
	]
	
	status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    
	created_at = models.DateTimeField(auto_now_add=True)
	borrower = models.ForeignKey(Borrower, models.CASCADE, related_name='loans')
	amount = models.DecimalField(max_digits=12, decimal_places=2)

upd. Решение оценили в 1 балл.
"""

from django.db.models import Sum

# Число заемщиков, имеющих закрытые займы (status = closed)
result = Borrower.objects.filter(loans__status=2).distinct().count()

# Число заемщиков, для которых существует хотя бы один заем, созданный в 2022 году.
result = Borrower.objects.filter(
    loans__created_at__year=2022
).distinct().count()

#Совокупный объем (amount) всех активных займов (status = active), принадлежащим заемщикам, которые зарегистрировались в 2021 году
sum_amount = Loan.objects.filter(
    status=1,
    borrower__created_at__year=2021
).aggregate(total=Sum('amount'))
result = sum_amount['total'] or 0


"""
5. Напишите функцию на Python, которая возвращает текущий публичный IP-адрес
компьютера (например, с использованием сервиса ifconfig.me).

upd. Решение оценили в 0.75 баллов. Хз, почему.
"""

import requests

TARGET_URL = 'https://ifconfig.me/'


def main():
    response = requests.get(TARGET_URL)
    if response.status_code == 200:
        print(f'IP-адрес: {response.text}')
    else:
        print('Something wrong...')


if __name__ == "__main__":
    main()


"""
6. Какие вы видите проблемы в следующем фрагменте кода? Как его следует исправить?
Подсказка: проблема не в POST/PUT и не в стилистике написания. Данный код часто приводит к неприятным побочным эффектам, которых можно избежать, сделав небольшую доработку.

@transaction.atomic
@api_view(['POST'])
def api_create_investor(request):
  investor = Investor.objects.create()
  investor_task.delay(investor.id)
  time.sleep(0.5) # эмуляция долгой работы метода - сама по себе проблемой не является
  return Response({"status": "OK"})


@shared_task
def investor_task(investor_id):
  investor = Investor.objects.get(pk=investor_id)
  investor.processed = True
  investor.save()
"""

"""
Ответ
Судя по delay() этот кусок кода из связки Django + Selery. Если в этом
ошибаюсь, то дальнейшие рассуждения скорее всего не верны.

На мой взгляд проблема в том, что в функции api_create_investor мы создаем
запись модели Investor в БД и затем запускаем асинхронно задачу
investor_task(), которая модифицирует запись investor, устанавливая для поля
processed значение True. Это может вызвать состояние гонки, когда несколько
потоков одновременно пытаются изменить одну и ту же запись в БД и привести к
ошибкам в работе приложения. Чтобы избежать этой проблемы, нужно явно
контролировать выполнение транзакции в функции investor_task делать при помощи
контекстного менеджера with transaction.atomic(), чтобы гарантировать, что
создание нового инвестора и его последующее изменение будут выполнены как
единое атомарное действие. Также можно использовать метод select_for_update()
для получения записи инвестора с блокировкой на запись, чтобы другие потоки не
смогли изменить запись одновременно с нашей задачей. В этом не уверен, не
смотрел что под капотом у контекстного менеджера. Возможно его будет
достаточно, atomic поймает ошибку и сделает rollback. А если все хорошо, то
commit. 

upd. Решение оценили в 0 баллов. Штош...
"""

@transaction.atomic
@api_view(['POST'])
def api_create_investor(request):
    investor = Investor.objects.create()
    investor_task.delay(investor.id)
    time.sleep(0.5) # эмуляция долгой работы метода - сама по себе проблемой не является
    return Response({"status": "OK"})


@shared_task
def investor_task(investor_id):
    with transaction.atomic():
        investor = Investor.objects.select_for_update().get(pk=investor_id)
        investor.processed = True
        investor.save()


"""
7. Какие вы видите проблемы в следующем фрагменте кода? Как его следует
исправить?
Подсказка: проблема не в похожих методах, не в POST/PUT и не в стилистике
написания. Данный код часто приводит к неприятным побочным эффектам,
которых можно избежать, сделав небольшую доработку.

@api_view(['POST'])
@transaction.atomic
def api_increase_a(request, investor_id):
  investor = get_object_or_404(Investor, pk=investor_id)
  investor.a += 100
  time.sleep(0.5) # эмуляция долгой работы метода - сама по себе проблемой не является
  investor.save()
  return Response({"status": "OK"})


@api_view(['POST'])
@transaction.atomic
def api_increase_b(request, investor_id):
  investor = get_object_or_404(Investor, pk=investor_id)
  investor.b += 100
  time.sleep(0.5) # эмуляция долгой работы метода - сама по себе проблемой не является
  investor.save()
  return Response({"status": "OK"})
"""

"""
Ответ
На мой взгляд код может привести к состоянию race condition при параллельном
выполнении запросов на изменение параметров a и b у одного и того же объекта
модели Investor. Чтобы избежать этого, нужно использовать метод
select_for_update, который блокирует выбранные объекты для изменения другими
процессами до тех пор, пока транзакция не завершится и блокировка не будет
снята.

upd. Решение оценили в 1 балл.
"""

from django.db import OperationalError


class IncreaseInProgress(Exception):
    pass


@api_view(['POST'])
@transaction.atomic
def api_increase_a(request, investor_id):
    try:
        investor = Investor.objects.select_for_update().get(pk=investor_id)
    except OperationalError:
        raise IncreaseInProgress
    investor.a += 100
    time.sleep(0.5)
    investor.save()
    return Response({"status": "OK"})

@api_view(['POST'])
@transaction.atomic
def api_increase_b(request, investor_id):
    try:
        investor = Investor.objects.select_for_update().get(pk=investor_id)
    except OperationalError:
        raise IncreaseInProgress
    investor.b += 100
    time.sleep(0.5)
    investor.save()
    return Response({"status": "OK"})


"""
8. Обработка Excel-файла
Задача: необходимо загрузить Excel-файл и посчитать статистику по заемщикам.
Файл содержит следующие колонки:
inn — ИНН заемщика (строка)
registration_date — дата регистрации компании (дата)
rating — рейтинг заемщика (число от 1 до 18)
amount — сумма займа (число)
Необходимо написать скрипт на Python, который загружает файл и выводит
следующие данные:
Сумма всех займов для компаний, зарегистрированных не позднее 2021 года.
Сумма займов для каждого из рейтингов (в виде таблицы с двумя колонками —
рейтинг и сумма) 

upd. Решение оценили в 1 балл
"""

# pip install pandas
# pip install openpyxl

from datetime import datetime

import pandas as pd

FILE_NAME = 'loans.xlsx'

df = pd.read_excel(FILE_NAME)

valid_records = df.registration_date <= datetime(2021, 12, 31)
total_amount = df[valid_records].amount.sum()
print(f'Сумма всех займов для компаний, зарегистрированных не позднее '
      f'2021 года: {total_amount}')

ratings_sum_by_loans = df.groupby(by=['rating']).amount.sum().reset_index()
print('Сумма займов для каждого из рейтингов:')
print(ratings_sum_by_loans.to_string(index=False))
