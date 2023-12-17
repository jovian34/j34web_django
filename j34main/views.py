from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required

from .models import Content, Category, AdditionalContent
from .forms import ContentForm


@xframe_options_exempt
def index(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "j34main/index.html", context)


def blogs(request):
    articles = Content.objects.all().order_by("-pub_date")
    context = {
        "articles": articles,
    }
    return render(request, "j34main/blogs.html", context)


def category_blogs(request, cat_pk):
    articles = Content.objects.filter(categories=cat_pk).order_by("-pub_date")[:4]
    category = Category.objects.get(pk=cat_pk)
    row_one = articles[0:2]
    row_two = articles[2:4]
    context = {
        "row_one": row_one,
        "row_two": row_two,
        "category": category,
    }
    return render(request, "j34main/partials/category_blogs.html", context)


def blog(request, blog_id):
    article = get_object_or_404(Content, pk=blog_id)
    add_content = AdditionalContent.objects.filter(main_content=blog_id).order_by(
        "order"
    )
    context = {
        "article": article,
        "add_content": add_content,
    }
    return render(request, "j34main/blog.html", context)


@login_required
def create_blog(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            add_blog = Content(
                title=form.cleaned_data["title"],
                sub_title=form.cleaned_data["sub_title"],
                featured_image=form.cleaned_data["featured_image"],
                image_caption=form.cleaned_data["image_caption"],
                teaser=form.cleaned_data["teaser"],
                content=form.cleaned_data["content"],
            )

            add_blog.save()
            add_blog.categories.set(form.cleaned_data["categories"])
            add_blog.save()
        return redirect("/j34")
    else:
        form = ContentForm()
        context = {
            "form": form,
        }
        return render(request, "j34main/create_blog.html", context=context)
