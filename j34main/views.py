from django.shortcuts import get_object_or_404, render

from .models import Content


def index(request):
    articles = Content.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'j34main/index.html', context)


def blog(request, blog_id):
    article = get_object_or_404(Content, pk=blog_id)
    context = {
        'article': article,
    }
    return render(request, 'j34main/blog.html', context)
