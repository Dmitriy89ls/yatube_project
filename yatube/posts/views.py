from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return HttpResponse(f'{slug}', context)
