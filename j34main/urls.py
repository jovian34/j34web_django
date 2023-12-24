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
    path(f"add_con/<int:add_con_id>/", views.add_content_partial, name="add_con"),
    path(f"edit_add_con_html/<int:add_con_id>/", views.edit_add_con_html, name="edit_add_con_html"),
    path(f"edit_add_con_markdown/<int:add_con_id>/", views.edit_add_con_markdown, name="edit_add_con_markdown"),    
]
