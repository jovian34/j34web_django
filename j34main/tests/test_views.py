import pytest

from django.contrib.auth.models import User
from django.utils import timezone

from ..models import Content, Category


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
    response = client.get("/j34/")
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


@pytest.fixture
def category_objs(client):
    cat1 = Category.objects.create(cat_name="Cat1")
    cat2 = Category.objects.create(cat_name="Cat2")
    cat3 = Category.objects.create(cat_name="Cat3")
    return cat1, cat2, cat3


@pytest.mark.django_db
def test_index_shows_all_categories(client, category_objs):
    response = client.get("/j34/")
    assert response.status_code == 200
    assert "Cat1" in str(response.content)
    assert "Cat2" in str(response.content)
    assert "Cat3" in str(response.content)


@pytest.fixture
def blog_objs(client, category_objs):
    blog1 = Content.objects.create(
        title="Blog Number One",
        sub_title="My first blog",
        pub_date=timezone.now(),
        teaser="A brief intro",
        content="The main content",
    )
    blog1.categories.set([category_objs[0], category_objs[1]])
    blog2 = Content.objects.create(
        title="Blog Number Two",
        sub_title="My second blog",
        pub_date=timezone.now(),
        teaser="A quick intro",
        content="The primary content",
    )
    blog2.categories.set([category_objs[0], category_objs[2]])
    return blog1, blog2


@pytest.mark.django_db
def test_single_blog_page_renders(client, blog_objs):
    response = client.get(f"/j34/blog/{blog_objs[0].id}/")
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
    response = client.get(f"/j34/category_blogs/{category_objs[0].id}/")
    assert response.status_code == 200
    assert "A quick intro" in str(response.content)


@pytest.mark.django_db
def test_category_blog_partial_does_not_render_other_category(
    client, blog_objs, category_objs
):
    response = client.get(f"/j34/category_blogs/{category_objs[1].id}/")
    assert response.status_code == 200
    assert "A quick intro" not in str(response.content)
    assert "A brief intro" in str(response.content)
