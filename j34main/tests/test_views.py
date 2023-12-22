import pytest

from django.contrib.auth.models import User
from django.urls import reverse

from ..models import Content, Category, AdditionalContent
from .view_fixtures import category_objs, blog_objs, blog2_additional_content


@pytest.mark.django_db
def test_index_page_renders(client):
    response = client.get("/j34/")
    assert response.status_code == 200
    assert "jovian34 LLC Blogs" in str(response.content)


def test_login_template_rendered(client):
    response = client.get("/accounts/login/")
    assert response.status_code == 200
    assert "registration/login.html" in response.template_name


@pytest.fixture
def logged_user_balius(client):
    user = User.objects.create_user(
        username="balius",
        email="balius@jovian34.com",
        password="Hdbwrwbrj7239293skjhkasH72!",
        first_name="Balius",
    )
    client.login(username="balius", password="Hdbwrwbrj7239293skjhkasH72!")
    return user


@pytest.mark.django_db
def test_logged_in_user_welcomed(client, logged_user_balius):
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "jovian34 LLC Blogs" in str(response.content)
    assert "Balius" in str(response.content)


@pytest.mark.django_db
def test_logging_out_redirects(client, logged_user_balius):
    response = client.post("/accounts/logout/", follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_logging_out_redirects_to_index(client, logged_user_balius):
    response = client.post("/accounts/logout/", follow=True)
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
    response = client.get(f"/j34/blog/{blog_objs.blog1.id}/")
    assert response.status_code == 200
    assert "The main content" in str(response.content)


@pytest.mark.django_db
def test_blog_list_renders(client, blog_objs):
    response = client.get("/j34/blogs/")
    assert response.status_code == 200
    assert "Blog Number One" in str(response.content)
    assert "A quick intro" not in str(response.content)
    assert "Blog Number Two" in str(response.content)


@pytest.mark.django_db
def test_category_blog_partial_renders(client, blog_objs, category_objs):
    response = client.get(f"/j34/category_blogs/{category_objs.cat1.id}/")
    assert response.status_code == 200
    assert "A quick intro" in str(response.content)


@pytest.mark.django_db
def test_category_blog_partial_does_not_render_other_category(
    client, blog_objs, category_objs
):
    response = client.get(f"/j34/category_blogs/{category_objs.cat2.id}/")
    assert response.status_code == 200
    assert "A quick intro" not in str(response.content)
    assert "A brief intro" in str(response.content)


@pytest.mark.django_db
def test_single_blog_page_renders_html(client, blog_objs):
    response = client.get(f"/j34/blog/{blog_objs.blog1.id}/")
    assert response.status_code == 200
    assert "<p>The main content" in str(response.content)


@pytest.mark.django_db
def test_single_blog_page_renders_primary_and_additional_content(
    client, blog_objs, blog2_additional_content
):
    response = client.get(f"/j34/blog/{blog_objs.blog2.id}/")
    assert response.status_code == 200
    assert "The primary content for blog two" in str(response.content)
    assert "Number five additional content" in str(response.content)
    assert "Number nine additional content" in str(response.content)


@pytest.mark.django_db
def test_create_new_blog(client, category_objs, logged_user_balius):
    response = client.post(
        reverse("create_blog"),
        {
            "title": "A Neil Diamond Christmas",
            "sub_title": "Hell YES he went there",
            "featured_image": "https://is1-ssl.mzstatic.com/image/thumb/Music128/v4/fb/20/77/fb2077de-14c8-c6e7-367f-33429d183c53/00602547673343.rgb.jpg/316x316bb.webp",
            "image_caption": "Neil Diamond's Christmas Album",
            "teaser": "Curated by Diamond and remastered by his longtime engineer, Bernie Becker.",
            "content": "A Neil Diamond Christmas is a 2022 collection of Christmas songs recorded by Neil Diamond.",
            "categories": (f"{category_objs.cat2.pk}", f"{category_objs.cat3.pk}")
        },
    )
    assert response.status_code == 302
    test_obj = Content.objects.last()
    assert test_obj.title == "A Neil Diamond Christmas"
    assert "2022 collection" in test_obj.content
    cats = [ cat.pk for cat in test_obj.categories.all() ]
    assert len(cats) == 2
    assert category_objs.cat2.pk in cats


@pytest.mark.django_db
def test_create_new_blog_fails_not_logged_in(client, category_objs):
    response = client.post(
        reverse("create_blog"),
        {
            "title": "A Neil Diamond Christmas",
            "sub_title": "Hell YES he went there",
            "featured_image": "https://is1-ssl.mzstatic.com/image/thumb/Music128/v4/fb/20/77/fb2077de-14c8-c6e7-367f-33429d183c53/00602547673343.rgb.jpg/316x316bb.webp",
            "image_caption": "Neil Diamond's Christmas Album",
            "teaser": "Curated by Diamond and remastered by his longtime engineer, Bernie Becker.",
            "content": "A Neil Diamond Christmas is a 2022 collection of Christmas songs recorded by Neil Diamond.",
            "categories": (f"{category_objs.cat2.pk}", f"{category_objs.cat3.pk}")
        },
    )
    assert response.status_code == 302
    test_obj = Content.objects.last()
    try:
        last_title = test_obj.title
    except AttributeError:
        assert True # no object should exist as there
    else:
        assert False

def test_create_blog_while_not_logged_in_forwards_to_login_form(client):
    response = client.get('/j34/create_blog/', follow=True)
    assert response.status_code == 200
    assert "Log In" in str(response.content)

@pytest.mark.django_db
def test_edit_blog_renders_filled_out_form(client, blog_objs, logged_user_balius):
    response = client.get(reverse("edit_blog", args=[blog_objs.blog2.pk]))
    assert response.status_code == 200
    assert "Blog Number Two" in str(response.content)

@pytest.mark.django_db
def test_blog_pages_includes_correct_edit_link_when_logged_on(client, blog_objs, logged_user_balius):
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