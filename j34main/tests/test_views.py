import pytest

from django.contrib.auth.models import User

from datetime import datetime, timedelta
from .. models import Content, Category


@pytest.mark.django_db
def test_index_page_renders(client):
    response = client.get("/j34/")
    assert response.status_code == 200
    assert "jovian34 LLC Blogs" in str(response.content)

def test_login_template_rendered(client):
    response = client.get("/accounts/login/")
    assert response.status_code == 200
    assert "registration/login.html" in response.template_name

@pytest.mark.django_db
def test_logged_in_user_welcomed(client):
    user = User.objects.create_user(
        username="balius",
        email="balius@jovian34.com",
        password="Hdbwrwbrj7239293skjhkasH72!",
        first_name="Balius"
    )
    client.login(
        username="balius",
        password="Hdbwrwbrj7239293skjhkasH72!"
    )
    response = client.get("/j34/")
    assert response.status_code == 200
    assert "jovian34 LLC Blogs" in str(response.content)
    assert "Balius" in str(response.content)

@pytest.mark.django_db
def test_logging_out_redirects(client):
    user = User.objects.create_user(
        username="balius",
        email="balius@jovian34.com",
        password="Hdbwrwbrj7239293skjhkasH72!",
        first_name="Balius"
    )
    client.login(
        username="balius",
        password="Hdbwrwbrj7239293skjhkasH72!"
    )
    response = client.post("/accounts/logout/", follow=False)
    assert response.status_code == 302

@pytest.mark.django_db
def test_logging_out_redirects_to_index(client):
    user = User.objects.create_user(
        username="balius",
        email="balius@jovian34.com",
        password="Hdbwrwbrj7239293skjhkasH72!",
        first_name="Balius"
    )
    client.login(
        username="balius",
        password="Hdbwrwbrj7239293skjhkasH72!"
    )
    response = client.post("/accounts/logout/", follow=True)
    assert response.status_code == 200
    assert "Staff login" in str(response.content)