import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # просто добавлю рандомной логики
    files_list = os.listdir('.')
    new_list = []
    for n, item in enumerate(files_list):
        new_list.append(f'Файл №{n+1}: ')
        new_list.append(f'{item} |||  ')
    return HttpResponse(new_list)
