from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Content, Category


@xframe_options_exempt
def index(request):
    categories = Category.objects.all()    
    context = {
        'categories': categories,
    }
    return render(request, 'j34main/index.html', context)


def blog(request, blog_id):
    article = get_object_or_404(Content, pk=blog_id)
    context = {
        'article': article,
    }
    return render(request, 'j34main/blog.html', context)


def blogs(request):
    articles = Content.objects.all().order_by('-pub_date')
    context = {
        'articles': articles,
    }
    return render(request, 'j34main/blogs.html', context)


def category_blogs(request, cat_pk):
    articles = Content.objects.filter(categories=cat_pk).order_by('-pub_date')[:4]
    row_one = articles[0:2]
    row_two = articles[2:4]
    context = {
        'row_one': row_one,
        'row_two': row_two,
    }
    return render(request, 'j34main/partials/category_blogs.html', context)