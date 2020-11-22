from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(f'blog/<int:blog_id>/', views.blog, name='blog'),
]
