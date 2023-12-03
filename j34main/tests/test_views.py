import pytest

from datetime import datetime, timedelta
from .. models import Content, Category


def test_top_level_site_forwards(client):
    response = client.get('')
    assert response.status_code == 302

@pytest.mark.django_db
def test_index_page_renders(client):
    response = client.get("/j34/")
    assert response.status_code == 200
    assert "jovian34 LLC Blogs" in str(response.content)

def test_login_template_rendered(client):
    response = client.get("/accounts/login/")
    assert response.status_code == 200
    assert "registration/login.html" in response.template_name