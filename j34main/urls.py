from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(f'blogs/', views.blogs, name='blogs'),
    path(f'blog/<int:blog_id>/', views.blog, name='blog'),
]
