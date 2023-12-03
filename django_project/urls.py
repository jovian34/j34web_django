import os
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(f"j34/", include("j34main.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path(f"{os.environ.get('ADMIN_WORD')}/", admin.site.urls),
]

admin.site.site_header = "jovian34 LLC"
admin.site.site_title = "jovian34 website"
admin.site.index_title = "jovian34 website"
