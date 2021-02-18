from django.shortcuts import render
from .models import icecream_db


def icecream_list(request):
    icecreams = ''
    for i in range(len(icecream_db)):
        icecreams += f"{icecream_db[i]['name']}<br>"
    context = {
        'icecreams': icecreams,
    }
    return render(request, 'icecream/icecream-list.html', context)


# Вторым аргументом эта функция должна принять переменную pk из path()
def icecream_detail(request):
    # Получите из icecream_db отдельно название
    # и отдельно описание запрошенного мороженого.
    # Сохраните их, соответственно, в переменные name и description
    name = ...
    description = ...
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-detail.html', context)
