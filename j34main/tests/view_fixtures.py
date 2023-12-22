import pytest

from collections import namedtuple
from django.utils import timezone

from ..models import Content, Category, AdditionalContent


@pytest.fixture
def category_objs(client):
    cat1 = Category.objects.create(cat_name="Cat1")
    cat2 = Category.objects.create(cat_name="Cat2")
    cat3 = Category.objects.create(cat_name="Cat3")
    CatObj = namedtuple("CatObj", "cat1 cat2 cat3")
    categories = CatObj(cat1=cat1, cat2=cat2, cat3=cat3)
    return categories


@pytest.fixture
def blog_objs(client, category_objs):
    blog1 = Content.objects.create(
        title="Blog Number One",
        sub_title="My first blog",
        pub_date=timezone.now(),
        teaser="A brief intro",
        content="The main content",
    )
    blog1.categories.set([category_objs.cat1, category_objs.cat2])
    blog2 = Content.objects.create(
        title="Blog Number Two",
        sub_title="My second blog",
        pub_date=timezone.now(),
        teaser="A quick intro",
        content="The primary content for blog two",
    )
    blog2.categories.set([category_objs.cat1, category_objs.cat3])
    BlogObj = namedtuple("BlogObj", "blog1 blog2")
    blogs = BlogObj(blog1=blog1, blog2=blog2)
    return blogs


@pytest.fixture
def blog2_additional_content(client, blog_objs):
    add2_5 = AdditionalContent.objects.create(
        main_content=blog_objs.blog2,
        order=5,
        additional_content="Number five additional content",
    )
    add2_9 = AdditionalContent.objects.create(
        main_content=blog_objs.blog2,
        order=9,
        additional_content="Number nine additional content",
    )
    AddContent = namedtuple("AddContent", "add2_5 add2_9")
    add_content = AddContent(add2_5=add2_5, add2_9=add2_9)
    return add_content
