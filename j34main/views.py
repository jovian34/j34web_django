from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required

from .models import Content, Category, AdditionalContent
from .forms import ContentForm, AdditionalContentHtmlForm, AdditionalContentMarkdownForm


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
        "categories": article.categories.all(),
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
        return redirect(reverse("index"))
    else:
        form = ContentForm()
        context = {
            "form": form,
        }
        return render(request, "j34main/create_blog.html", context=context)


@login_required
def edit_blog(request, blog_id):
    orig_blog = Content.objects.get(pk=blog_id)
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            orig_blog.title=form.cleaned_data["title"]
            orig_blog.sub_title=form.cleaned_data["sub_title"]
            orig_blog.featured_image=form.cleaned_data["featured_image"]
            orig_blog.image_caption=form.cleaned_data["image_caption"]
            orig_blog.teaser=form.cleaned_data["teaser"]
            orig_blog.content=form.cleaned_data["content"]
            orig_blog.categories.set(form.cleaned_data["categories"])
            orig_blog.save()
        return redirect(reverse("blog", args=[blog_id]))
    else:
        add_cons = AdditionalContent.objects.filter(main_content=blog_id)
        form_main = ContentForm(
            initial={
                "title": orig_blog.title,
                "sub_title": orig_blog.sub_title,
                "featured_image": orig_blog.featured_image,
                "image_caption": orig_blog.image_caption,
                "teaser": orig_blog.teaser,
                "content": orig_blog.content,
                "categories": orig_blog.categories.all(),
            }
        )
        form_add_html = AdditionalContentHtmlForm(
            initial={
                "order": add_cons.order,
                "additional_content": add_cons.additional_content,
            }
        )
        form_add_markdown = AdditionalContentMarkdownForm(
            initial={
                "order": add_cons.order,
                "additional_content": add_cons.additional_content,
            }
        )
        context = {
            "form_main": form_main,
            "form_add_html": form_add_html,
            "form_add_markdown": form_add_markdown,
            "add_cons": add_cons,
        }
        return render(request, "j34main/edit_blog.html", context=context)
