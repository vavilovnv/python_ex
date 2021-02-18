from django.shortcuts import render
from .models import icecream_db


def icecream_list(request):
    icecreams = ''
    for i in range(len(icecream_db)):
        icecreams += f"<a href='{i}/'>{icecream_db[i]['name']}</a><br>"
    context = {
        'icecreams': icecreams,
    }
    return render(request, 'icecream/icecream-list.html', context)


def icecream_detail(request, pk):
    name = icecream_db[pk]['name']
    description = icecream_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-detail.html', context)
