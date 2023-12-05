import pytest


def test_top_level_site_forwards(client):
    response = client.get("", follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_top_level_site_forwards_to_index(client):
    response = client.get("", follow=True)
    assert response.status_code == 200
    assert "jovian34 LLC Blogs" in str(response.content)
