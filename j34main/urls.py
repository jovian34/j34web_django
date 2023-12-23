from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(f"blogs/", views.blogs, name="blogs"),
    path(f"blog/<int:blog_id>/", views.blog, name="blog"),
    path(f"create_blog/", views.create_blog, name="create_blog"),
    path(f"edit_blog/<int:blog_id>/", views.edit_blog, name="edit_blog"),
    # partials
    path(f"category_blogs/<int:cat_pk>/", views.category_blogs, name="category_blogs"),
    
]
