# Текст задания: https://stepik.org/lesson/24476/step/3?unit=6781

# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом
# числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

import requests

api_url = "http://numbersapi.com/"
params = {
     'json': 'True'
}

with open('input.txt') as f:
    for line in f:
        number = line.strip()
        res = requests.get(api_url + number + '/math', params)
        print('Interesting' if res.json()['found'] == True else 'Boring')



