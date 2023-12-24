import pytest

from django.urls import reverse

from ..models import Content
from .fixtures import category_objs, blog_objs, blog2_additional_content, logged_user_balius


@pytest.mark.django_db
def test_index_page_renders(client):
    response = client.get("/j34/")
    assert response.status_code == 200
    assert "jovian34 LLC Blogs" in str(response.content)


def test_login_template_rendered(client):
    response = client.get(reverse("login"))
    assert response.status_code == 200
    assert "registration/login.html" in response.template_name


@pytest.mark.django_db
def test_logged_in_user_welcomed(client, logged_user_balius):
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "jovian34 LLC Blogs" in str(response.content)
    assert "Balius" in str(response.content)


@pytest.mark.django_db
def test_logging_out_redirects(client, logged_user_balius):
    response = client.post(reverse("logout"), follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_logging_out_redirects_to_index(client, logged_user_balius):
    response = client.post(reverse("logout"), follow=True)
    assert response.status_code == 200
    assert "Staff login" in str(response.content)


@pytest.mark.django_db
def test_index_shows_all_categories(client, category_objs):
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "Cat1" in str(response.content)
    assert "Cat2" in str(response.content)
    assert "Cat3" in str(response.content)


@pytest.mark.django_db
def test_single_blog_page_renders(client, blog_objs):
    response = client.get(reverse("blog", args=[blog_objs.blog1.id]))
    assert response.status_code == 200
    assert "The main content" in str(response.content)


@pytest.mark.django_db
def test_blog_list_renders(client, blog_objs):
    response = client.get(reverse("blogs"))
    assert response.status_code == 200
    assert "Blog Number One" in str(response.content)
    assert "A quick intro" not in str(response.content)
    assert "Blog Number Two" in str(response.content)


@pytest.mark.django_db
def test_category_blog_partial_renders(client, blog_objs, category_objs):
    response = client.get(reverse("category_blogs", args=[category_objs.cat1.id]))
    assert response.status_code == 200
    assert "A quick intro" in str(response.content)


@pytest.mark.django_db
def test_category_blog_partial_does_not_render_other_category(
    client, blog_objs, category_objs
):
    response = client.get(reverse("category_blogs", args=[category_objs.cat2.id]))
    assert response.status_code == 200
    assert "A quick intro" not in str(response.content)
    assert "A brief intro" in str(response.content)


@pytest.mark.django_db
def test_single_blog_page_renders_html(client, blog_objs, category_objs):
    response = client.get(reverse("blog", args=[blog_objs.blog1.id]))
    assert response.status_code == 200
    assert "<p>The main content" in str(response.content)
    assert category_objs.cat1.cat_name in str(response.content)


@pytest.mark.django_db
def test_single_blog_page_renders_primary_and_additional_content(
    client, blog_objs, blog2_additional_content
):
    response = client.get(reverse("blog", args=[blog_objs.blog2.id]))
    assert response.status_code == 200
    assert "The primary content for blog two" in str(response.content)
    assert "Number five additional content" in str(response.content)
    assert "Number nine additional content" in str(response.content)


@pytest.mark.django_db
def test_create_new_blog(client, category_objs, logged_user_balius):
    response = client.post(
        reverse("create_blog"),
        {
            "title": "Manually keyed blog title One",
            "sub_title": "This is the first blog keyed in manually",
            "featured_image": "https://live.staticflickr.com/65535/53413424892_4c0442a468_c.jpg",
            "image_caption": "Lexus Bargesser layup",
            "teaser": "This is a tease of the first manually entered blog.",
            "content": "This is the primary content of the first manually entered blog.",
            "categories": (f"{category_objs.cat2.pk}", f"{category_objs.cat3.pk}"),
        },
    )
    assert response.status_code == 302
    test_obj = Content.objects.last()
    assert test_obj.title == "Manually keyed blog title One"
    assert "first manually entered" in test_obj.content
    cats = [cat.pk for cat in test_obj.categories.all()]
    assert len(cats) == 2
    assert category_objs.cat2.pk in cats

 
@pytest.mark.django_db
def test_create_new_blog_fails_not_logged_in(client, category_objs):
    response = client.post(
        reverse("create_blog"),
        {
            "title": "Manually keyed blog title Two",
            "sub_title": "This is the second blog keyed in manually",
            "featured_image": "https://live.staticflickr.com/65535/53413424892_4c0442a468_c.jpg",
            "image_caption": "Lexus Bargesser layup",
            "teaser": "This is a tease of the second manually entered blog.",
            "content": "This is the primary content of the second manually entered blog.",
            "categories": (f"{category_objs.cat2.pk}", f"{category_objs.cat3.pk}"),
        },
    )
    assert response.status_code == 302
    test_obj = Content.objects.last()
    try:
        last_title = test_obj.title
    except AttributeError:
        assert True  # no object should exist as no logged-in user fixture was passed
    else:
        assert False


def test_create_blog_while_not_logged_in_forwards_to_login_form(client):
    response = client.get(reverse("create_blog"), follow=True)
    assert response.status_code == 200
    assert "Log In" in str(response.content)


@pytest.mark.django_db
def test_edit_blog_renders_filled_out_form(client, blog_objs, logged_user_balius):
    response = client.get(reverse("edit_blog", args=[blog_objs.blog2.pk]))
    assert response.status_code == 200
    assert "Blog Number Two" in str(response.content)


@pytest.mark.django_db
def test_blog_pages_includes_correct_edit_link_when_logged_on(
    client, blog_objs, logged_user_balius
):
    response = client.get(reverse("blog", args=[blog_objs.blog1.pk]))
    assert response.status_code == 200
    assert reverse("edit_blog", args=[blog_objs.blog1.pk]) in str(response.content)


@pytest.mark.django_db
def test_blog_page_omits_edit_link_when_not_logged_in(client, blog_objs):
    response = client.get(reverse("blog", args=[blog_objs.blog1.pk]))
    assert response.status_code == 200
    assert reverse("edit_blog", args=[blog_objs.blog1.pk]) not in str(response.content)


@pytest.mark.django_db
def test_edit_blog_redirects_when_not_logged_in(client, blog_objs):
    response = client.get(reverse("edit_blog", args=[blog_objs.blog2.pk]))
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_blog_redirects_to_index_when_not_logged_in(client, blog_objs):
    response = client.get(reverse("edit_blog", args=[blog_objs.blog2.pk]), follow=True)
    assert response.status_code == 200
    assert "Staff login" in str(response.content)

@pytest.mark.django_db
def test_edit_blog_submits_edited_content(client, category_objs, blog_objs, logged_user_balius):
    response = client.post(
        reverse("edit_blog", args=[blog_objs.blog2.pk]),
        {
            "title": "Blog Number Two",
            "sub_title": "My second blog",
            "teaser": "A quick intro",
            "featured_image": "https://www.billboard.com/wp-content/uploads/2022/09/taylor-swift-NSAI-billboard-2022-1548.jpg",
            "image_caption": "edited caption for image",
            "content": "Edited content",
            "categories": [category_objs.cat1.pk, category_objs.cat2.pk],
        },
        follow=True,
    )
    assert response.status_code == 200
    assert "Title:" not in str(response.content)
    assert "Blog Number Two" in str(response.content)
    assert "Edited content" in str(response.content)
    assert category_objs.cat2.cat_name in str(response.content)
