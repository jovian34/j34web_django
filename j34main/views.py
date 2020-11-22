from django.shortcuts import render

from .models import Content


def split_paras(articles):
    pass


def index(request):
    articles = Content.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'j34main/index.html', context)
