from django.shortcuts import render
from icecream.models import icecream_db
from anfisa.models import friends_db
# Из файла services приложения anfisa импортируйте функцию what_temperature
from anfisa.services import what_weather, what_temperature


def index(request):
    icecreams = ''
    friends = ''
    city_weather = ''
    friend_output = ''
    selected_icecream = ''
    # Подготовили к выводу чистую температуру
    parsed_temperature = ''

    for friend in friends_db:
        friends += (f'<input type="radio" name="friend"'
                   f' required value="{friend}">{friend}<br>')

    for i in range(len(icecream_db)):
        ice_form = (f'<input type="radio" name="icecream" required'
                    f' value="{icecream_db[i]["name"]}">{icecream_db[i]["name"]}')

        ice_link = f'<a href="icecream/{i}/">Узнать состав</a>'
        icecreams += f'{ice_form} | {ice_link} <br>'

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        selected_icecream = request.POST['icecream']
        city = friends_db[selected_friend]
        weather = what_weather(city)

        # Получите температуру и сохраните ее в parsed_temperature
        parsed_temperature = what_temperature(weather)
        friend_output = f'{selected_friend}, тебе прислали {selected_icecream}!'
        city_weather = f'В городе {city} погода: {weather}'

    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
        # Передайте значение parsed_temperature в шаблон
        'parsed_temperature', parsed_temperature
    }
    return render(request, 'homepage/index.html', context)
